---
layout: archive
title: "Coordination of Large Robot Teams in Automated Warehouses"
permalink: /research/warehouse/
author_profile: true
---

{% include base_path %}

(**This page is still under construction.**)

<div>
    <div id="wrapper" style="float:left;width:250pt;padding:10px;"> 
        <video id="single-agent" width="300pt"  autoplay loop controls> 
            <source type="video/mp4" src="https://jiaoyangli.me/images/Single+_800agents-8x.mp4" /> 
        </video>
        <figcaption>Traditional single-agent solver</figcaption>
        <video id="multi-agent" width="300pt"  autoplay loop controls> 
            <source type="video/mp4" src="https://jiaoyangli.me/images/PBS_w=10_800agents-8x.mp4" /> 
        </video>
        <figcaption>Our MAPF solver</figcaption>
        <div class="clear"></div> 
    </div>
    Today, in automated warehouses, 
    mobile robots already autonomously move inventory pods or flat packages from one location to another. 
    Finding low-cost paths for the robots in real-time is essential for the effectiveness of such systems. 
    However, MAPF is only the “one-shot” variant of the actual problem in many applications. 
    Typically, after an agent reaches its goal location, it does not stop and wait there forever. 
    Instead, it is assigned a new goal location and required to keep moving, 
    which is referred to as lifelong MAPF and characterized by agents constantly being assigned new goal locations. 
    There are three challenges in this problem, namely 
    how to assign tasks to agents, 
    how to decompose the lifelong problem to one-shot MAPF problems and solve it efficiently, and
    how to handle robot dynamics and uncertainties during execution.
</div>

## Combined Task and Path Planning

Automated warehousing systems need to continually assign delivery tasks and collision-free paths to robots 
in an online manner. Traditional task assignment algorithms ignore collisions among agents, 
which can generate task assignments that eventually lead to costly collision-free paths or even no collision-free paths.
We develop various of combined task and path planning algorithms with different properties 
(e.g., optimal, complete, capable of handling time-window constraints, etc.) that suit for different scenarios.

Relevant publications: 
[1] [Decoupled online task assignment and path planning](https://jiaoyangli.me/publications/MaAAMAS17), 
[2] [Decoupled offline task assignment and path planning](https://jiaoyangli.me/publications/LiuAAMAS19), 
[3] [CBS-based optimal task and path planning](https://jiaoyangli.me/publications/ZhongICRA22), 
[4] [LNS-based task and path planning](https://jiaoyangli.me/publications/XuIROS22),
[5] [Deadline-aware task and path planning](https://jiaoyangli.me/publications/HuangHSI22), and
[6] [column generation for tasks with time windows](https://arxiv.org/abs/2103.08835 "Preprint 2021").


## Scalability and Solution Quality

Highlights:
The RHCR algorithm proposed in [1] can produce high-quality solutions for **1,000 agents** (= **38.9% of the empty cells** on the map) for simulated warehouse instances. 
The left videos show the performance of 800 agents on the same map with traditional single-agent solver and RHCR.

Relevant publications: 
[1] [rolling-horizon collision resolution](https://jiaoyangli.me/publications/LiAAAI21lifelong).




## Combined Planning and Execution

Relevant publications: 
[1] [Different MAPF models for warehouses](https://jiaoyangli.me/publications/VaramballySoCS22)