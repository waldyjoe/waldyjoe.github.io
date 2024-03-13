import sys

from ortools.linear_solver import pywraplp
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

from utils import get_travel_time

class Solver(object):

    def __init__(self, df, capacity):

        self.data = self.create_data_model(df, capacity)
        self.data_vrp = self.create_data_model_vrp(df, 0)

    def create_data_model(self, df, capacity):
        data = {}
        weights = df["total_cbm"].to_list()
        data["weights"] = weights
        data["items"] = list(range(len(weights)))
        data["bins"] = data["items"]
        data["bin_capacity"] = capacity
        orderIds = df["delivery_id"].to_list()
        data["items mapping"] = {}
        for elem in data["items"]:
            data["items mapping"][elem] = orderIds[elem]
        return data

    def solve_min_trucks(self):

        output = {"Total" : 0, "Assignment" : {}}

        # Create the mip solver with the SCIP backend.
        solver = pywraplp.Solver.CreateSolver("SCIP")

        if not solver:
            return

        # Variables
        # x[i, j] = 1 if item i is packed in bin j.
        x = {}
        for i in self.data["items"]:
            for j in self.data["bins"]:
                x[(i, j)] = solver.IntVar(0, 1, "x_%i_%i" % (i, j))

        # y[j] = 1 if bin j is used.
        y = {}
        for j in self.data["bins"]:
            y[j] = solver.IntVar(0, 1, "y[%i]" % j)

        # Constraints
        # Each item must be in exactly one bin.
        for i in self.data["items"]:
            solver.Add(sum(x[i, j] for j in self.data["bins"]) == 1)

        # The amount packed in each bin cannot exceed its capacity.
        for j in self.data["bins"]:
            solver.Add(
                sum(x[(i, j)] * self.data["weights"][i] for i in self.data["items"])
                <= y[j] * self.data["bin_capacity"]
            )

        # Objective: minimize the number of bins used.
        solver.Minimize(solver.Sum([y[j] for j in self.data["bins"]]))

        print(f"Solving with {solver.SolverVersion()}")
        status = solver.Solve()

        if status == pywraplp.Solver.OPTIMAL:
            num_bins = 0
            for j in self.data["bins"]:
                if y[j].solution_value() == 1:
                    bin_items = []
                    bin_weight = 0
                    for i in self.data["items"]:
                        if x[i, j].solution_value() > 0:
                            bin_items.append(i)
                            bin_weight += self.data["weights"][i]
                    if bin_items:
                        num_bins += 1
                        output["Assignment"]["T" + str(j + 1)] = {"Items": bin_items, "Total weights": bin_weight }
                        # print("Bin number", j)
                        # print("  Items packed:", bin_items)
                        # print("  Total weight:", bin_weight)
                        # print()
            # print()
            # print("Number of bins used:", num_bins)
            # print("Time = ", solver.WallTime(), " milliseconds")
            output["Total"] = num_bins
            return output
        else:
            print("The problem does not have an optimal solution.")
            return None


    def create_data_model_vrp(self, df, trucksNum):
        data = {}

        location_master_table = {}
        for idx, row in df.iterrows():
            location_master_table[row['zip']] = (row['lat'], row['lng'])
        # Add depot
        location_master_table[92804] = (33.81826, -117.97506)

        idx_to_zip = {}
        idx_to_zip[0] = 92804
        for i in range(len(location_master_table.keys())):
            idx_to_zip[i+1] = list(location_master_table.keys())[i]

        data["time_matrix"] = []
        data["time_windows"] = []

        for i in range(len(idx_to_zip.keys())):
            temp_list = []
            for j in range(len(idx_to_zip.keys())):
                start_coord = location_master_table[idx_to_zip[i]]
                end_coord = location_master_table[idx_to_zip[j]]
                # add 30 mins for service time at each location
                temp_list.append(get_travel_time(start_coord, end_coord) + 30)
            data["time_matrix"].append(temp_list)

            data["time_windows"].append((0,600))

        data["num_vehicles"] = trucksNum
        data["depot"] = 0
        return data


    def solve_vrp(self, numTrucks):

        self.data_vrp["num_vehicles"] = numTrucks


        def print_solution(data, manager, routing, solution):
            """Prints solution on console."""
            print(f"Objective: {solution.ObjectiveValue()}")
            time_dimension = routing.GetDimensionOrDie("Time")
            total_time = 0
            for vehicle_id in range(data["num_vehicles"]):
                index = routing.Start(vehicle_id)
                plan_output = f"Route for vehicle {vehicle_id}:\n"
                while not routing.IsEnd(index):
                    time_var = time_dimension.CumulVar(index)
                    plan_output += (
                        f"{manager.IndexToNode(index)}"
                        f" Time({solution.Min(time_var)},{solution.Max(time_var)})"
                        " -> "
                    )
                    index = solution.Value(routing.NextVar(index))
                time_var = time_dimension.CumulVar(index)
                plan_output += (
                    f"{manager.IndexToNode(index)}"
                    f" Time({solution.Min(time_var)},{solution.Max(time_var)})\n"
                )
                plan_output += f"Time of the route: {solution.Min(time_var)}min\n"
                print(plan_output)
                total_time += solution.Min(time_var)
            print(f"Total time of all routes: {total_time}min")

        # Create the routing index manager.
        manager = pywrapcp.RoutingIndexManager(
            len(self.data_vrp["time_matrix"]), self.data_vrp["num_vehicles"], self.data_vrp["depot"]
        )

        # Create Routing Model.
        routing = pywrapcp.RoutingModel(manager)

        # Create and register a transit callback.
        def time_callback(from_index, to_index):
            """Returns the travel time between the two nodes."""
            # Convert from routing variable Index to time matrix NodeIndex.
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return self.data_vrp["time_matrix"][from_node][to_node]

        transit_callback_index = routing.RegisterTransitCallback(time_callback)

        # Define cost of each arc.
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Add Time Windows constraint.
        time = "Time"
        routing.AddDimension(
            transit_callback_index,
            0,  # allow waiting time
            600,  # maximum time per vehicle
            False,  # Don't force start cumul to zero.
            time,
        )
        time_dimension = routing.GetDimensionOrDie(time)
        # Add time window constraints for each location except depot.
        for location_idx, time_window in enumerate(self.data_vrp["time_windows"]):
            if location_idx == self.data_vrp["depot"]:
                continue
            index = manager.NodeToIndex(location_idx)
            time_dimension.CumulVar(index).SetRange(time_window[0], time_window[1])
        # Add time window constraints for each vehicle start node.
        depot_idx = self.data_vrp["depot"]
        for vehicle_id in range(self.data_vrp["num_vehicles"]):
            index = routing.Start(vehicle_id)
            time_dimension.CumulVar(index).SetRange(
                self.data_vrp["time_windows"][depot_idx][0], self.data_vrp["time_windows"][depot_idx][1]
            )

        # Instantiate route start and end times to produce feasible times.
        for i in range(self.data_vrp["num_vehicles"]):
            routing.AddVariableMinimizedByFinalizer(
                time_dimension.CumulVar(routing.Start(i))
            )
            routing.AddVariableMinimizedByFinalizer(time_dimension.CumulVar(routing.End(i)))

        # Setting first solution heuristic.
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
        )

        # Solve the problem.
        solution = routing.SolveWithParameters(search_parameters)

        # Print solution on console.
        if solution:
            # can be activated for debuggin purposes
            # print_solution(self.data_vrp, manager, routing, solution)
            print("Optimal Solution found")
            return "Solved"
        else:
            return "Not Solved"