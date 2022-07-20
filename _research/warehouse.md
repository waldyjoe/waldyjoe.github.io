---
layout: archive
title: "Coordination of Large Robot Teams in Automated Warehouses"
permalink: /research/warehouse/
author_profile: true
---

{% include base_path %}

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
