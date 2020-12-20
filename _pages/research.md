---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}


## Symmetry Reasoning for Multi-Agent Path Finding
<img src="/images/rectangle.png" title="rectangle symmetry" style="float:left;width:250pt;padding-right:10px;" />
Multi-Agent Path Finding (MAPF) is a challenging combinatorial problem that asks us to plan collision-free paths for a team of cooperative agents. One of the reasons MAPF problems are so hard to solve is due to a phenomena called pairwise path symmetry, which occurs when two agents have many equivalent paths, all of which appear promising, but which are
pairwise incompatible because they result in a collision. 
The symmetry arises commonly in practice and can produce an exponential explosion in the space of possible collision resolutions, leading to unacceptable runtimes for currently state-of-the-art MAPF algorithms that employ heuristic search, such as Conflict-based Search (CBS).
To break symmetries, we propose a variety of constraint-based reasoning techniques, to detect the symmetries as they arise and to efficiently eliminate, in a single branching step, all permutations of two currently assigned but pairwise incompatible paths.
 
Relevant publications: 
[1] [rectangle symmetry](https://aaai.org/ojs/index.php/AAAI/article/view/4565 "AAAI 2019"), 
[2] [corridor and target symmetries](https://www.aaai.org/ojs/index.php/ICAPS/article/view/6661/6515 "ICAPS 2020"), 
[3] [automatic symmetry reasoning by mutex propagation](https://www.aaai.org/ojs/index.php/ICAPS/article/view/6677/6531 "ICAPS 2020"), 
[3] [mutex propagation for SAT-based MAPF](https://jiaoyang-li.github.io/files/2020-PRIMA.pdf "PRIMA 2020"), 
[4] [symmetry reasoning for k-robust MAPF](https://jiaoyang-li.github.io/files/2021-AAAI-4.pdf "AAAI 2021"), and 
[5] [symmetry reasoning with bounded-suboptimal CBS](https://arxiv.org/abs/2010.01367 "AAAI 2021").


## Heuristics for Multi-Agent Path Finding with Conflict-Based Search
<img src="/images/heuristics.png" title="heuristic graph" style="float:left;width:250pt;padding-right:10px;" />
Conflict-Based Search (CBS) and its enhancements are among the strongest algorithms for Multi-Agent Path Finding. 
However, existing variants of CBS do not use any heuristics that estimate future work.
Introducing admissibles heuristics to guide the high-level search of CBS can significantly reduce the size of the CBS search tree and runtime.
Introducing more informed but potentially inadmissible heuritics to guide the high-level search of bounded-suboptimal CBS can further reduce the size of its search tree and runtime. 

Relevant publications: 
[1] [CG heuristicy for CBS](https://aaai.org/ocs/index.php/ICAPS/ICAPS18/paper/view/17735/16965 "ICAPS 2018"), 
[2] [DG and WDG heuristics for CBS](https://www.ijcai.org/proceedings/2019/0063.pdf "IJCAI 2019"), and
[3] [inadmissible heuristic for bounded-suboptimal CBS](https://arxiv.org/abs/2010.01367 "AAAI 2021").


