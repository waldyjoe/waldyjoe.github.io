---
layout: archive
title: "Intelligent Traffic Management"
permalink: /research/traffic/
author_profile: true
---

{% include base_path %}

## MAPF for Traffic Management
<img src="/images/flatland.gif" title="flatland demo" style="float:left;width:250pt;padding-right:10px;" />

MAPF can also be used for traffic management for autonomous vehicle, trains, or airplanes. 
This can reduce traffic congestion, energy consumption, and air pollution. 
The main challenges of applying MAPF to traffic management systems are two-fold. 
First, the systems are neither perfect nor deterministic. 
For example, the environment might cause unexpected disturbances, 
the communication network might not be stable, 
the agents might have incomplete knowledge of the environment, 
and the agents might not be able to execute their deterministic MAPF plans perfectly. 
We need to take such uncertainties into account during path planning and generate robust plans. 
Second, the sysmtem needs to operate thousands of (or even more) agents in real-time, 
so extremely efficient MAPF algorithms are required.          

Highlights:
The MAPF-based software we developed for the NeurIPS'20 Flatland Challenge in [1] can plan collision-free paths for **more than 3000 agents** within a few minutes and
deliver deadlock-free actions **in real-time** during execution that are robust to unexpexted delays. It outperformed all other solutions, including all reinforcement learning solutions, to **win the overall first place** in both rounds. A comparison of our solution with top reinforcement learning solutions can be found in [2].

Relevant publications: 
[1] [railway planing and replaning](https://jiaoyangli.me/files/2021-ICAPS.pdf "ICAPS 2021") (**winner of the NeurIPS'20 Flatland Challenge**),
[2] [railway planing and replaning with MAPF and MARL](http://proceedings.mlr.press/v133/laurent21a.html), and
[3] [airport taxiway planning](https://arc.aiaa.org/doi/abs/10.2514/6.2019-2930 "AIAA 2019").         
