---
layout: archive
title: "MAPF Generalizations for Heterogeneous and Nonholonomic Robots"
permalink: /research/drones/
author_profile: true
---

{% include base_path %}
<style>
td,th {
   border: none!important;
}
</style>

|                              Arena          |  Drones |
|:-------------------------------------------:|:-------------------------:|
| ![](https://jiaoyangli.me/images/arena.gif) |  ![](https://jiaoyangli.me/images/arena.gif) |



<p style="text-align:center;">
    <img src="https://jiaoyangli.me/images/arena.gif" title="mobile robots" width="200pt" alt="arena"/>
    <img src="https://jiaoyangli.me/images/drone_side.gif" title="mobile robots" width="200pt" />
    <img src="https://jiaoyangli.me/images/drone_top.gif" title="mobile robots" width="400pt" />
</p>

 <img src="https://jiaoyangli.me/images/bar.gif" title="robotic arms" style="width:250pt" />
  <figcaption>Multi-arm assembly</figcaption>
Agents in MAPF are unrealistic and homogeneous, in the sense that each agent occupies exactly one vertex at any timestep and traverses exactly one edge or wait at its current vertex from one timestep to the next one. In the real world, however, agents might be of different shapes and have different kinematic constraints. Moreover, agents sometimes are required to move to their goal locations while maintaining a desired formation (i.e., spatial pattern), in order to reduce the system cost, increase the robustness and efficiency of the system. 
Notably, in addition to the traditional mobile robots/drones that navigate in a 2D/3D space, MAPF can be also used for planning trajectories for robotic arms! See the demo on the left (the work is under review at RAL/ICRA2022).

## From Continuous Space to Discrete Graphs

Relevant publications: 
[1] [agents of different shapes](https://aaai.org/ojs/index.php/AAAI/article/view/4756 "AAAI 2019"), 
[2] [agents of high-dimensional, nonlinear, and nonholonomic dynamics](https://ojs.aaai.org/index.php/AAAI/article/view/17340 "AAAI 2021"), and
[3] [agents that move in formation](http://ifaamas.org/Proceedings/aamas2020/pdfs/p726.pdf "AAMAS 2020").
