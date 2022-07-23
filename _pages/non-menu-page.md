---
permalink: /non-menu-page/
layout: archive
author_profile: true
redirect_from: 
  - "/nmp/"
  - "/nmp.html"
---
<!--title: "Page not in menu"
excerpt: "This is a page not in the main menu"-->
{% include base_path %}
<!--{% include toc %}-->

{% include base_path %}

My research focuses on developing fundamental algorithms that enable large teams of autonomous agents
to accomplish collaborative tasks intelligently in dynamic environments.
Applications of my research include
mobile robot coordination for automated warehousing and, in general, nonholonomic robot teams,
drone swarm control,
multi-arm assembly,
character control in video games,
and traffic management for airports, railway networks, and road intersections with autonomous cars.

<link rel="stylesheet" href="../assets/css/imagehovertext.css">

<style>
/* Float four columns side by side */
.column {
  float: left;
  width: 33%;
  padding: 0 10px;
}

/* Remove extra left and right margins, due to padding in columns */
.row {margin: 0 -5px;}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

.card {
  /* Add shadows to create the "card" effect */
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  padding: 0.75rem;
  flex-direction: column;
  max-width: 100%;
  border-radius: 5px;
  text-align: center;
}

/* On mouse-over, add a deeper shadow */
.card:hover {
  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.2);
}

/* Add some padding inside the card container 
.card .container {
  padding: 2px 16px;
  flex-direction: column;
  flex: 1;
  display: flex;
  text-align: left;
}*/

.is-flex-wrap {
  flex-wrap: wrap;
  /*flex-grow: 0;*/
  /*justify-content: space-around;*/
  /*justify-content: flex-start;*/
}
</style>
<!--
<div class="row">
  <div class="column">
    <div class="card">
      <a href="https://jiaoyangli.me/research/mapf/">
        <b>Foundations of Multi-Agent Path Finding (MAPF)</b>
      </a>
      <img src="https://jiaoyangli.me/images/mapf-demo.gif" alt="MAPF" width="200pt">
      <div class="container">
        We develop principled algorithms to solve challenging MAPF instances 
        via a variety of AI and optimization technologies, such as
        constraint reasoning, heuristic search, stochastic local search, and machine learning.
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <img src="https://jiaoyangli.me/images/warehouse-5x.gif" alt="MAPF" width="200pt">
      <div class="container">
        <a href="https://jiaoyangli.me/research/mapf/">
        <b>Coordination of Large Robot Teams in Automated Warehouses</b>
        </a>
        We develop principled algorithms to solve challenging MAPF instances 
        via a variety of AI and optimization technologies, such as
        constraint reasoning, heuristic search, stochastic local search, and machine learning.
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <img src="https://jiaoyangli.me/images/bar.gif" alt="MAPF" width="200pt">
      <div class="container">
        <a href="https://jiaoyangli.me/research/mapf/">
        <b>Foundations of Multi-Agent Path Finding (MAPF)</b>
        </a>
        We develop principled algorithms to solve challenging MAPF instances 
        via a variety of AI and optimization technologies, such as
        constraint reasoning, heuristic search, stochastic local search, and machine learning.
      </div>
    </div>
  </div>
</div>
-->


<div class="flex-container is-flex-wrap">
        <!-- MAPF -->
                <div class="flex-child card">
<a href="https://jiaoyangli.me/research/mapf/">
                    <p class="image__title"> Foundations of Multi-Agent Path Finding (MAPF) </p>
                    <img src="../images/mapf-demo.gif" alt="MAPF" style="float:left;width:200pt;" />
                    We developing principled algorithms to solve challenging MAPF instances 
                    via a variety of AI and optimization technologies, such as
                    constraint reasoning, heuristic search, stochastic local search, and machine learning.
</a>
                </div>
        <!-- warehouse -->
            <div class="flex-child card">
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
        <!-- robotic arms -->
            <div class="flex-child card">
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
        <!-- traffic -->
            <div class="flex-child card">
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
        <!-- drones -->
            <div class="flex-child card">
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
        <!-- others -->
            <div class="flex-child card">
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
