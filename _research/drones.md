---
layout: archive
title: "Drone Swarms Coordination"
permalink: /research/mapf/
author_profile: true
---

{% include base_path %}

## MAPF for Heterogeneous and Nonholonomic Robots
<div id="wrapper" align="center" style="float:left;width:150pt;padding-right:10px;"> 
  <img src="/images/arena.gif" title="mobile robots" style="width:250pt" />
  <figcaption>Mobile robot team</figcaption>
  <img src="/images/bar.gif" title="robotic arms" style="width:250pt" />
  <figcaption>Multi-arm assembly</figcaption>
</div>
Agents in MAPF are unrealistic and homogeneous, in the sense that each agent occupies exactly one vertex at any timestep and traverses exactly one edge or wait at its current vertex from one timestep to the next one. In the real world, however, agents might be of different shapes and have different kinematic constraints. Moreover, agents sometimes are required to move to their goal locations while maintaining a desired formation (i.e., spatial pattern), in order to reduce the system cost, increase the robustness and efficiency of the system. 
Notably, in addition to the traditional mobile robots/drones that navigate in a 2D/3D space, MAPF can be also used for planning trajectories for robotic arms! See the demo on the left (the work is under review at RAL/ICRA2022).


Relevant publications: 
[1] [agents of different shapes](https://aaai.org/ojs/index.php/AAAI/article/view/4756 "AAAI 2019"), 
[2] [agents of high-dimensional, nonlinear, and nonholonomic dynamics](https://ojs.aaai.org/index.php/AAAI/article/view/17340 "AAAI 2021"), and
[3] [agents that move in formation](http://ifaamas.org/Proceedings/aamas2020/pdfs/p726.pdf "AAMAS 2020").
