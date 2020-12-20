---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}


## Symmetry Reasoning for Multi-Agent Path Finding

<p align="center">
  <img src='/images/rectangle.png' width='500'>
</p>

Multi-Agent Path Finding (MAPF) is a challenging combinatorial problem that asks us to plan collision-free paths for a team of cooperative agents. One of the reasons MAPF problems are so hard to solve is due to a phenomena called pairwise path symmetry, which occurs when two agents have many equivalent paths, all of which appear promising, but which are
pairwise incompatible because they result in a collision. 
The symmetry arises commonly in practice and can produce an exponential explosion in the space of possible collision resolutions, leading to unacceptable runtimes for currently state-of-the-art MAPF algorithms that employ heuristic search, such as Conflict-based Search (CBS).
To break symmetries, we propose a variety of constraint-based reasoning techniques, to detect the symmetries as they arise and to efficiently eliminate, in a single branching step, all permutations of two currently assigned but pairwise incompatible paths.

Relevant publications: [rectangle symmetry](https://aaai.org/ojs/index.php/AAAI/article/view/4565), [corridor and target symmetries](https://www.aaai.org/ojs/index.php/ICAPS/article/view/6661/6515 "Download pdf"), [automatic symmetry reasoning by mutex propagation](https://www.aaai.org/ojs/index.php/ICAPS/article/view/6677/6531), [symmetry reasoning for k-robust MAPF](https://jiaoyang-li.github.io/files/2021-AAAI-4.pdf), and [symmetry reasoning for bounded-suboptimal MAPF algorithms](https://arxiv.org/abs/2010.01367)

{% for post in site.research %}
  {% include archive-single.html %}
{% endfor %}

