---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}

<img src="/images/mapf-demo.gif" title="mapf demo" style="float:right;width:200pt;padding-left:10px;" />
Recent advances in robotics have laid the foundation for building large-scale multi-agent systems. A great deal of research has focused on coordinating agents to fulfill different types of tasks. In my research, I focus on one fundamental task - to navigate teams of agents in a shared environment to their goal locations without colliding with obstacles or other agents.
One well-studied abstract model for this problem is known as **Multi-Agent Path Finding (MAPF)**. It is defined on a general graph with given start and goal vertices for agents on this graph. Each agent is allowed to wait at its current vertex or move to an adjacent vertex from one discrete timestep to the next one. We are asked to find a path for each agent such that no two agents are at the same vertex or cross the same edge at any timestep (because this would result in a collision). The objective is to minimize the sum of the arrival times of all agents.

My research concentrates on developing AI techniques to bridge the gap between MAPF and real-world applications. My main contributions are summarized as follows: 
- Improving the scalability of MAPF algorithms:
  - Developing **symmetry reasoning** techniques to speed up optimal and bounded-suboptimal MAPF algorithms.
  - Introducing **heuristics** to conflict-based search to speed up optimal and bounded-suboptimal MAPF algorithms.
- Applying MAPF to various multi-agent systems:
  - Applying MAPF to **automated warehousing**.
  - Applying MAPF to **traffic management**.
  - Applying MAPF to multi-robot systems with **heterogeneous and nonholonomic robots**.

## Symmetry Reasoning for MAPF
<img src="/images/rectangle.png" title="rectangle symmetry" style="float:left;width:250pt;padding-right:10px;" />
One of the reasons MAPF problems are so hard to solve is due to a phenomena called pairwise path symmetry, which occurs when two agents have many equivalent paths, all of which appear promising, but which are
pairwise incompatible because they result in a collision. 
The symmetry arises commonly in practice and can produce an exponential explosion in the space of possible collision resolutions, leading to unacceptable runtimes for currently state-of-the-art MAPF algorithms that employ heuristic search, such as Conflict-based Search (CBS).
To break symmetries, we propose a variety of constraint-based reasoning techniques, to detect the symmetries as they arise and to efficiently eliminate, in a single branching step, all permutations of two currently assigned but pairwise incompatible paths.     
 
Highlights: 
The addition of the symmetry-reasoning techniques proposed in [3] can reduce the number of expanded nodes and runtime of the optimal algorithm CBS by up to **4 orders of magnitude** and thus can handle up to **30 times more agents** than possible before within one minute.         

Relevant publications: 
[1] [rectangle symmetry](https://aaai.org/ojs/index.php/AAAI/article/view/4565 "AAAI 2019"), 
[2] [corridor and target symmetries](https://www.aaai.org/ojs/index.php/ICAPS/article/view/6661/6515 "ICAPS 2020"), 
[3] [generalized rectangle, target, and corridor symmetry reasoning](https://arxiv.org/abs/2103.07116 "Preprint 2021"), 
[4] [automatic symmetry reasoning by mutex propagation](https://www.aaai.org/ojs/index.php/ICAPS/article/view/6677/6531 "ICAPS 2020") (**ICAPS'20 outstanding student paper**), 
[5] [mutex propagation for SAT-based MAPF](https://jiaoyang-li.github.io/files/2020-PRIMA.pdf "PRIMA 2020"), 
[6] [symmetry reasoning for k-robust MAPF](https://jiaoyang-li.github.io/files/2021-AAAI-4.pdf "AAAI 2021"), and 
[7] [symmetry reasoning with bounded-suboptimal CBS](https://arxiv.org/abs/2010.01367 "AAAI 2021").


## Heuristics for MAPF with Conflict-Based Search
<img src="/images/heuristics.png" title="heuristic graph" style="float:left;width:250pt;padding-right:10px;" />
Conflict-Based Search (CBS) and its enhancements are among the strongest algorithms for MAPF. 
However, existing variants of CBS do not use any heuristics that estimate future work.
Introducing admissibles heuristics to guide the high-level search of CBS can significantly reduce the size of the CBS search tree and its runtime.
Introducing more informed but potentially inadmissible heuritics to guide the high-level search of bounded-suboptimal CBS with Explicit Estimation Search can further reduce the size of its search tree and its runtime.           

Highlights: 
The addition of the admissible heuristics proposed in [2] can reduce the number of expanded nodes and runtime of CBS by up to **a factor of 50** and thus an handle up to **3 times more agents** than possible before within one minute.
The bounded-suboptimal MAPF algorithm proposed in [3] can find solutions that are **provably at most 2% worse than optimal** with **1,000 agents** in one minute, while, on the
same map, state-of-the-art optimal algorithms can handle at most 200 agents.             

Relevant publications: 
[1] [CG heuristicy for CBS](https://aaai.org/ocs/index.php/ICAPS/ICAPS18/paper/view/17735/16965 "ICAPS 2018"), 
[2] [DG and WDG heuristics for CBS](https://www.ijcai.org/proceedings/2019/0063.pdf "IJCAI 2019"), and
[3] [inadmissible heuristic for bounded-suboptimal CBS](https://arxiv.org/abs/2010.01367 "AAAI 2021").


## Lifelong MAPF for Automated Warehousing
<!--
<img src="https://jiaoyang-li.github.io/images/PBS_w=10_800agents-8x.mp4" title="warehouse demo" style="float:left;width:250pt;padding-right:10px;" />
<figure class="video_container">
  <video width="320" autoplay loop>
    <source src="https://jiaoyang-li.github.io/images/Single+_800agents-8x.mp4" type="video/mp4">
    <source src="https://jiaoyang-li.github.io/images/PBS_w=10_800agents-8x.mp4" type="video/mp4">
  </video>
</figure>
<video width="320" height="240" controls>
  <source src="ttps://jiaoyang-li.github.io/images/warehouse.mkv" type="video/mkv">
</video>
--> 



 <div id="wrapper" align="center" style="float:left;width:250pt;padding-right:10px;"> 
     <video id="single-agent" width="250pt"  autoplay loop controls> 
         <source type="video/mp4" src="https://jiaoyang-li.github.io/images/Single+_800agents-8x.mp4" /> 
     </video>
    <figcaption>Traditional single-agent solver</figcaption>
     <video id="multi-agent" width="250pt"  autoplay loop controls> 
         <source type="video/mp4" src="https://jiaoyang-li.github.io/images/PBS_w=10_800agents-8x.mp4" /> 
     </video>
     <figcaption>Our MAPF solver</figcaption>
     <div class="clear"></div> 
 </div>
Today, in automated warehouses, mobile robots already autonomously move inventory pods or flat packages from one location to another. Finding low-cost paths for the robots in real-time is essential for the effectiveness of such systems. However, MAPF is only the “one-shot” variant of the actual problem in many applications. Typically, after an agent reaches its goal location, it does not stop and wait there forever. Instead, it is assigned a new goal location and required to keep moving, which is referred to as lifelong MAPF and characterized by agents constantly being assigned new goal locations. There are two challenges in this problem, namely how to assign tasks to agents and how to decompose the lifelong problem to one-shot MAPF problems.               

Highlights:
The RHCR algorithm propoased in [3] can produce high-quality solutions for **1,000 agents** (= **38.9% of the empty cells** on the map) for simulated warehouse instances. The left videos show the performance of 800 agents on the same map with tradional single-agent solver and RHCR.

Relevant publications: 
[1] [MAPF with online task assignment](https://dl.acm.org/citation.cfm?id=3091243 "AAMAS 2017"), 
[2] [MAPF with offline task assignment](http://www.ifaamas.org/Proceedings/aamas2019/pdfs/p1152.pdf "AAMAS 2019"), 
[3] [rolling-horizon collision resolution](https://arxiv.org/abs/2005.07371 "AAAI 2021"), and
[4] [column generation for tasks with time windows](https://arxiv.org/abs/2103.08835 "Preprint 2021").

## MAPF for Traffic Management
<img src="/images/flatland.gif" title="flatland demo" style="float:left;width:250pt;padding-right:10px;" />

MAPF can also be used for traffic manangement for autonomous vehicle, trains, or airplanes. This can reduce traffic congestion, energy consumption, and air pollution. The main challenges of applying MAPF to traffic management systems are two-fold. First, the systems are neither perfect nor deterministic. For example, the environment might cause unexpected disturbances, the communication network might not be stable, the agents might have incomplete knowledge of the environment, and the agents might not be able to execute their deterministic MAPF plans perfectly. We need to take such uncertainties into account during path planning and generate robust plans. Second, the sysmtem needs to operate thousands of (or even more) agents in real-time, so extremely efficient MAPF algorithms are required.          

Highlights:
The MAPF-based software we developed for the NeurIPS'20 Flatland Challenge in [1] can plan collision-free paths for **more than 3000 agents** within a few minutes and
deliver deadlock-free actions **in real-time** during execution that are robust to unexpexted delays. It outperformed all other solutions, including all reinforcement learning solutions, to **win the overall first place** in both rounds. A comparison of our solution with top reinforcement learning solutions can be found in [2].

Relevant publications: 
[1] [railway planing and replaning](https://jiaoyangli.me/files/2021-ICAPS.pdf "ICAPS 2021") (**winner of the NeurIPS'20 Flatland Challenge**),
[2] [railway planing and replaning with MAPF and MARL](http://proceedings.mlr.press/v133/laurent21a.html), and
[3] [airport taxiway planning](https://arc.aiaa.org/doi/abs/10.2514/6.2019-2930 "AIAA 2019").         

## MAPF for Heterogeneous and Nonholonomic Robots
<div id="wrapper" align="center" style="float:left;width:250pt;padding-right:10px;"> 
  <img src="/images/drone_side.gif" title="drones" style="width:130pt" />
  <figcaption>Top view</figcaption>
  <img src="/images/drone_top.gif" title="drones" style="width:250pt" />
  <figcaption>Side view</figcaption>
</div>
Agents in MAPF are homogeneous, in the sense that each agent occupies exactly one vertex at any timestep and traverses exactly one edge or wait at its current vertex from one timestep to the next one. In the real world, however, agents might be of different shapes and have different kinematic constraints. In addition, agents sometimes are required to move to their goal locations while maintaining a desired formation (i.e., spatial pattern), in order to reduce the system cost, increase the robustness and efficiency of the system.

Relevant publications: 
[1] [agents of different shapes](https://aaai.org/ojs/index.php/AAAI/article/view/4756 "AAAI 2019"), 
[2] [agents of high-dimensional, nonlinear, and nonholonomic dynamics](https://arxiv.org/abs/2012.09052 "AAAI 2021"), and
[3] [agents that move in formation](http://ifaamas.org/Proceedings/aamas2020/pdfs/p726.pdf "AAMAS 2020").
