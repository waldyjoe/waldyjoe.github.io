---
layout: archive
title: "People"
permalink: /people/
author_profile: true
---

{% include base_path %}

<img src="https://jiaoyangli.me/images/logo-white-background.png" title="logo" style="float:right;width:200pt;padding-left:10px;"  alt="logo"/>

.card {
    border: 1px solid #ddd;
    border-radius: 6px;
    max-width: 350px;
    text-align: center;
    margin-top: 60px;
}
.card_img {
    width: 120px;
    height: 120px;
    overflow: hidden;
    border-radius: 100%;
    margin: -60px auto 0;
}
.card_img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.card_info {
    padding-bottom: 20px;
}
a {
  text-decoration: none;
  color: red;
}
a:hover{
  color: black;
}

# ARCS Lab embers
## Current Members
### PhD Students
<div class="card"> <!-- Here I create a New Div with class name card -->
    <div class="card_img">
        <img src="https://jiaoyangli.me/images/yulunzhang.jpg" alt="user-image">
    </div>
    <div class="card_info">
        <h2>Yulun Zhang</h2>
    </div>
</div>


<div class="container">
    <div class="tile is-ancestor is-flex-wrap">
        <!-- MAPF -->
        <div class="tile is-parent">
            <div class="tile is-child card">
                <p class="image__title"> Foundations of Multi-Agent Path Finding (MAPF) </p>
                <div class="image">
                    <a href="https://jiaoyangli.me/research/mapf/">
                        <img class="image__img" src="../images/mapf-demo.gif" alt="MAPF">
                        <div class="image__overlay image__overlay--blur">
                            <p class="image__description">
                                Developing principled algorithms to solve challenging MAPF instances
                                via a variety of AI and optimization technologies, such as
                                constraint reasoning, heuristic search, stochastic local search, and machine learning.
                            </p>
                        </div>
                    </a>
                </div>
            </div>
        </div>
        <!-- warehouse -->
        <div class="tile is-parent">
            <div class="tile is-child card">
                <p class="image__title"> Coordination of Large Robot Teams in Automated Warehouses </p>
                <div class="image">
                    <a href="https://jiaoyangli.me/research/warehouse/">
                        <img class="image__img" src="https://jiaoyangli.me/images/warehouse-5x.gif" alt="MAPF">
                        <div class="image__overlay image__overlay--blur">
                            <p class="image__description">
                                Combing task planning, path planning, and execution
                                to coordinate thousands of mobile robots
                                to fulfill delivery tasks in automated warehouses.
                            </p>
                        </div>
                    </a>
                </div>
            </div>
        </div>
        <!-- robotic arms -->
        <div class="tile is-parent">
            <div class="tile is-child card">
                <p class="image__title"> Multi-Arm Assembly </p>
                <div class="image">
                    <a href="https://jiaoyangli.me/research/arm/">
                        <img class="image__img" src="../images/bar.gif" alt="Robotic Arms">
                        <div class="image__overlay image__overlay--blur">
                            <p class="image__description">
                                Developing combined task and motion planning frameworks
                                to jointly plan safe, low-cost plans
                                for a team of robots to assemble complex spatial structures.
                            </p>
                        </div>
                    </a>
                </div>
            </div>
        </div>
        <!-- traffic -->
        <div class="tile is-parent">
            <div class="tile is-child card">
                <p class="image__title"> Intelligent Traffic Management </p>
                <div class="image">
                    <a href="https://jiaoyangli.me/research/traffic/">
                        <img class="image__img" src="../images/flatland.gif" alt="Railway Planning">
                        <div class="image__overlay image__overlay--blur">
                            <p class="image__description">
                                Developing intelligent planning systems to coordinate
                                trains, airplanes, autonomous vehicle, etc. on complex road networks under uncertainty.
                            </p>
                        </div>
                    </a>
                </div>
            </div>
        </div>
        <!-- drones -->
        <div class="tile is-parent">
            <div class="tile is-child card">
                <p class="image__title"> MAPF Generalizations for Heterogeneous and Nonholonomic Robots </p>
                <div class="image">
                    <a href="https://jiaoyangli.me/research/drones/">
                        <img class="image__img" src="../images/drone_side.gif" alt="Drones">
                        <!--<img class="image__img" src="../images/drone_top.gif" alt="Robotic Arms">-->
                        <div class="image__overlay image__overlay--blur">
                            <p class="image__description">
                                Develop principled algorithms for solving MAPF.
                                Drone Swarms Coordination
                            </p>
                        </div>
                    </a>
                </div>
            </div>
        </div>
        <!-- others -->
        <div class="tile is-parent">
            <div class="tile is-child card">
                <p class="image__title"> Other Projects </p>
                <div class="image">
                    <a href="https://jiaoyangli.me/research/others/">
                        <img class="image__img" src="../images/3d-fastmap.png" alt="FastMap">
                        <div class="image__overlay image__overlay--blur">
                            <p class="image__description"> Graph embeddings, multi-agent meeting problems, etc. </p>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>

<br style = "line-height:5;">