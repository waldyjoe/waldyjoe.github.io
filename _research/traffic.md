---
layout: archive
title: "Intelligent Traffic Management"
permalink: /research/traffic/
author_profile: true
---

{% include base_path %}

<div id="wrapper" style="float: left; width: 50%; padding: 10px; text-align: center"> 
    <img src="https://jiaoyangli.me/images/flatland.gif" alt="flatland" style="height:120pt;width:auto" />
    <figcaption>Rail planning and replanning</figcaption>
</div>
<div id="wrapper" style="float: left; width: 50%; padding: 10px; text-align: center">
    <img src="../images/airport-2x.gif" alt="airport" style="height:120pt;width:auto" />
    <figcaption>Airport superface coordination</figcaption>
</div>

MAPF can be used for traffic management for autonomous vehicle, trains, or airplanes. 
This can reduce traffic congestion, energy consumption, and air pollution. 
The main challenges of applying MAPF to traffic management systems are two-fold. 
First, the systems are neither perfect nor deterministic. 
For example, the environment might cause unexpected disturbances, 
the communication network might not be stable, 
the agents might have incomplete knowledge of the environment, 
and the agents might not be able to execute their deterministic MAPF plans perfectly. 
We need to take such uncertainties into account during path planning and generate robust plans. 
Second, the system needs to operate thousands of (or even more) agents in real-time, 
so extremely efficient MAPF algorithms are required.          

Highlights:
The MAPF-based software we developed for the NeurIPS'20 Flatland Challenge in [1] can plan collision-free paths for **more than 3000 agents** within a few minutes and
deliver deadlock-free actions **in real-time** during execution that are robust to unexpected delays. It outperformed all other solutions, including all reinforcement learning solutions, to **win the overall first place** in both rounds. A comparison of our solution with top reinforcement learning solutions can be found in [2].

Relevant publications: 
[1] [railway planing and replanning](https://jiaoyangli.me/publications/LiICAPS21) (**winner of the NeurIPS'20 Flatland Challenge**),
[2] [railway planing and replanning with MAPF and MARL](https://jiaoyangli.me/publications/Laurent21), and
[3] [airport taxiway planning](https://jiaoyangli.me/publications/LiAIAA19).         

<div style="float: right;">
    <button onclick="location.href='https://jiaoyangli.me/research/'" type="button">Back to the Research page</button>
</div>