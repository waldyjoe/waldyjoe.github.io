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

<!--<link rel="stylesheet" href="https://jiaoyangli.me/assets/css/imagehovertext.css">-->

<style>
.flex-container {
    display: flex;
}

.is-flex-wrap {
  flex-wrap: wrap;
  /*flex-grow: 0;*/
  /*justify-content: space-around;*/
  /*justify-content: flex-start;*/
}

/*.container{flex-grow:1;margin:0 auto;position:relative;width:auto}*/
.flex-child{
    padding:.75rem;
    min-width:220px;
    flex: 1;
    margin-right: 20px;
    margin-top: 20px;
    align-items: center
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

.image {
    align-self: center;
    align-items: center;
    position: relative;
    width: 250px;
    margin-top: 1.0em;
}

.image__title {
    font-size: 1em;
    font-weight: bold;
    align-self: center;
    text-align: center;
    margin-top: 1.0em;
}

.image__img {
    display: block;
    width: 100%;
}

.image__description {
    margin-top: 0.25em;
    margin-left: 0.25em;
    margin-right: 0.25em;
    text-align: center;
}

.image__overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    color: #ffffff;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.25s;
}

.image__overlay--blur {
    backdrop-filter: blur(5px);
}

.image__overlay > * {
    transform: translateY(20px);
    transition: transform 0.25s;
}

.image__overlay:hover {
    opacity: 1;
}

.image__overlay:hover > * {
    transform: translateY(0);
}
</style>


<div class="flex-container is-flex-wrap">
    <!-- MAPF -->
    <div class="flex-child card">
        <p class="image__title"> Foundations of Multi-Agent Path Finding (MAPF) </p>
        <div class="image">
            <a href="https://jiaoyangli.me/research/mapf/">            
                <img class="image__img" src="https://jiaoyangli.me/images/mapf-demo.gif" alt="MAPF" />
                <div class="image__overlay image__overlay--blur">
                    <p class="image__description">
                        We develop principled algorithms to solve challenging MAPF instances 
                        via a variety of AI and optimization technologies, such as
                        constraint reasoning, heuristic search, stochastic local search, and machine learning.
                    </p>
                </div>
            </a>
        </div>
    </div>
    <!-- warehouse -->
    <div class="flex-child card">
        <p class="image__title"> Coordination of Large Robot Teams in Automated Warehouses </p>
        <div class="image">
            <a href="https://jiaoyangli.me/research/warehouse/">
                <img class="image__img" src="https://jiaoyangli.me/images/warehouse-5x.gif" alt="warehouse">
                <div class="image__overlay image__overlay--blur">
                    <p class="image__description">
                        We combine task planning, path planning, and execution
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
                <img class="image__img" src="https://jiaoyangli.me/images/bar.gif" alt="Robotic Arms">
                <div class="image__overlay image__overlay--blur">
                    <p class="image__description">
                        We develop combined task and motion planning frameworks
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
                <img class="image__img" src="https://jiaoyangli.me/images/flatland.gif" alt="Railway Planning">
                <div class="image__overlay image__overlay--blur">
                    <p class="image__description">
                        We develop intelligent planning systems to coordinate
                        trains, airplanes, autonomous vehicle, etc. on complex road networks under uncertainty.
                    </p>
                </div>
            </a>
        </div>
    </div>
    <!-- drones -->
    <div class="flex-child card">
        <p class="image__title"> Planning for Heterogeneous and Nonholonomic Robots </p>
        <div class="image">
            <a href="https://jiaoyangli.me/research/drones/">
                <img class="image__img" src="../images/drone_side.gif" alt="Drones">
                <div class="image__overlay image__overlay--blur">
                    <p class="image__description">
                        We generalize MAPF algorithms to coordinate teams of 
                        heterogeneous and nonholonomic robots 
                        by considering various practical constraints from robotics.
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
                <img class="image__img" src="https://jiaoyangli.me/images/3d-fastmap.png" alt="FastMap">
                <div class="image__overlay image__overlay--blur">
                    <p class="image__description"> 
                        We perform other planning and search related projects, 
                        such as graph embeddings, multi-agent meeting problems, etc. 
                    </p>
                </div>
            </a>
        </div>
    </div>
</div>
