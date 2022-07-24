---
layout: archive
title: "Planning for Heterogeneous and Nonholonomic Robots"
permalink: /research/drones/
author_profile: true
---

{% include base_path %}

(**This page is still under construction.**)

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
<div style="display: flex; flex-wrap: wrap; text-align: center">
    <div style="min-width:310px;flex: 1;margin: 5px;">
        <img src="https://jiaoyangli.me/images/arena.gif" width="200px" alt="arena"/>
        <figcaption>Searching in 2D spaces.</figcaption>
    </div>
    <div style="min-width:310px;flex: 1;margin: 5px;">
        <img src="https://jiaoyangli.me/images/3Dmaze.gif" width="308.88px" alt="3D maze"/>
        <figcaption>Searching in 3D spaces.</figcaption>
    </div>
    <div style="min-width:310px;flex: 1;margin: 5px;">
        <img src="https://jiaoyangli.me/images/bar.gif" width="200px" alt="arm" />
        <figcaption>Searching in high-dimensional spaces.</figcaption>
    </div>
</div>
<div style="clear:both;"></div>

Relevant publications: 
[1] [agents of different shapes](https://jiaoyangli.me/publications/LiAAAI19large),
[2] [agents of nonholonomic dynamics](https://jiaoyangli.me/publications/ChenAAAI21s2m2), 
[3] [time-robust plans](https://jiaoyangli.me/publications/ChenAAAI21robust), and
[4] [snake-like agents](https://jiaoyangli.me/publications/ChenSoCS22).


## Moving in formation
<p style="text-align:center;">
    <img src="/images/formation-random-4x.gif" style="max-height:200pt" alt="formation-random"/>
    <img src="/images/formation-tight-4x.gif" style="max-height:200pt" alt="formation-tight"/>
    <img src="/images/formation-wide-4x.gif" style="max-height:200pt" alt="formation-wide"/>
</p>

[1] [agents that move in formation](http://ifaamas.org/Proceedings/aamas2020/pdfs/p726.pdf "AAMAS 2020").

<div style="float: right;">
    <button onclick="location.href='https://jiaoyangli.me/research/'" type="button">Back to the Research page</button>
</div>