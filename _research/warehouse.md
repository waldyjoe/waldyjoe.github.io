---
layout: archive
title: "Coordination of Large Robot Teams in Automated Warehouses"
permalink: /research/warehouse/
author_profile: true
---

{% include base_path %}

<!--
<img src="https://jiaoyangli.me/images/PBS_w=10_800agents-8x.mp4" title="warehouse demo" style="float:left;width:250pt;padding-right:10px;" />
<figure class="video_container">
  <video width="320" autoplay loop>
    <source src="https://jiaoyangli.me/images/Single+_800agents-8x.mp4" type="video/mp4">
    <source src="https://jiaoyangli.me/images/PBS_w=10_800agents-8x.mp4" type="video/mp4">
  </video>
</figure>
<video width="320" height="240" controls>
  <source src="https://jiaoyangli.me/images/images/warehouse.mkv" type="video/mkv">
</video>
--> 

(**This page is still under construction.**)


<div id="wrapper" align="center" style="float:left;width:250pt;padding-right:10px;"> 
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
Today, in automated warehouses, mobile robots already autonomously move inventory pods or flat packages from one location to another. Finding low-cost paths for the robots in real-time is essential for the effectiveness of such systems. However, MAPF is only the “one-shot” variant of the actual problem in many applications. Typically, after an agent reaches its goal location, it does not stop and wait there forever. Instead, it is assigned a new goal location and required to keep moving, which is referred to as lifelong MAPF and characterized by agents constantly being assigned new goal locations. 
There are two challenges in this problem, namely how to assign tasks to agents and how to decompose the lifelong problem to one-shot MAPF problems.               


## Scalability and Solution Quality

Highlights:
The RHCR algorithm proposed in [1] can produce high-quality solutions for **1,000 agents** (= **38.9% of the empty cells** on the map) for simulated warehouse instances. 
The left videos show the performance of 800 agents on the same map with traditional single-agent solver and RHCR.

Relevant publications: 
[1] [rolling-horizon collision resolution](https://jiaoyangli.me/publications/LiAAAI21lifelong).


## Combined Task and Path Planning

Relevant publications: 
[1] [Decoupled online task assignment and path planning](https://jiaoyangli.me/publications/MaAAMAS17), 
[2] [Decoupled offline task assignment and path planning](https://jiaoyangli.me/publications/LiuAAMAS19), 
[3] [CBS-based optimal task and path planning](https://jiaoyangli.me/publications/ZhongICRA22), 
[4] [LNS-based task and path planning](https://jiaoyangli.me/publications/XuIROS22),
[5] [Deadline-aware task and path planning](https://jiaoyangli.me/publications/HuangHSI22), and
[6] [column generation for tasks with time windows](https://arxiv.org/abs/2103.08835 "Preprint 2021").


## Combined Planning and Execution

Relevant publications: 
[1] [Different MAPF models for warehouses](https://jiaoyangli.me/publications/VaramballySoCS22)