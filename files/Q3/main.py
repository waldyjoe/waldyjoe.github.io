
import datetime
import pandas as pd
import sys

from solver import Solver



if __name__ == "__main__":

    raw_file = "Q3 LA Deliveries.csv"

    df = pd.read_csv(raw_file)
    df['delivery_date'] = pd.to_datetime(df['delivery_date'])
    unique_delivery_dates = df['delivery_date'].unique()


    # Mission 1
    # formulate the problem as bin-packing problem
    trucks_per_day = {}
    for date in unique_delivery_dates:
        df_daily_order = df[df['delivery_date'] == date]
        solver = Solver(df_daily_order, 20)
        output = solver.solve_min_trucks()
        trucks_per_day[date] = output["Total"]


    minTruck = max(trucks_per_day.values())
    # Minimum number of trucks needed is the maximum number of trucks needed to fullfil the largest daily order
    print("Minimum number of trucks needed: ", minTruck)

    # Mission 2
    # formulate the problem as VRP with Time Windows
    daily_status = {}
    for date in unique_delivery_dates:
        df_daily_order = df[df['delivery_date'] == date]
        solver = Solver(df_daily_order, 20)
        status = solver.solve_vrp(minTruck)
        daily_status[date] = status



    rows = []
    for date in daily_status.keys():
        rows.append([date, daily_status[status]])

    df_assignment = pd.Dataframe(rows, columns=['Date', 'VRP Solved'])
    df_assignment.to_excel("output.xlsx", index=False)










