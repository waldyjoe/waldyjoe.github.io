---
layout: archive
title: "MAPF Generalizations for Heterogeneous and Nonholonomic Robots"
permalink: /research/drones/
author_profile: true
---

{% include base_path %}


Agents in MAPF are unrealistic and homogeneous, 
in the sense that each agent occupies exactly one vertex at any timestep and 
traverses exactly one edge or wait at its current vertex from one timestep to the next one. 
In the real world, however, agents might be of different shapes and have different kinematic constraints. 
Moreover, agents sometimes are required to move to their goal locations 
while maintaining a desired formation (i.e., spatial pattern), 
in order to reduce the system cost, increase the robustness and efficiency of the system. 
Notably, in addition to the traditional mobile robots/drones that navigate in a 2D/3D space, 
MAPF can be also used for planning trajectories for robotic arms!

## From Discrete Graphs and Timesteps to Continuous Space and Time
<p style="text-align:center;">
    <img src="https://jiaoyangli.me/images/arena.gif" width="200pt" alt="arena"/>
    <!--<img src="https://jiaoyangli.me/images/maze.gif" width="200pt" alt="maze"/>-->
    <img src="https://jiaoyangli.me/images/3Dmaze.gif" width="200pt" alt="3Dmaze"/>
    <!--<img src="https://jiaoyangli.me/images/drone_top.gif" width="400pt" alt="drone-side" />
    <img src="https://jiaoyangli.me/images/drone_side.gif" width="200pt" alt="drone-top" />-->
    <img src="https://jiaoyangli.me/images/bar.gif" width="200pt" alt="arm" />
</p>


Relevant publications: 
[1] [agents of different shapes](https://jiaoyangli.me/publications/LiAAAI19large),
[2] [agents of nonholonomic dynamics](https://jiaoyangli.me/publications/ChenAAAI21s2m2), 
[3] [time-robust plans](https://jiaoyangli.me/publications/ChenAAAI21robust), and
[4] [snake-like agents](https://jiaoyangli.me/publications/ChenSoCS22).


## Moving in formation
[3] [agents that move in formation](http://ifaamas.org/Proceedings/aamas2020/pdfs/p726.pdf "AAMAS 2020").

