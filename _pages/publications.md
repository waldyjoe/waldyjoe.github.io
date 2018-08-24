---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

5. Hang Ma, Glenn Wager, Ariel Felner, Jiaoyang Li, T. K. Satish Kumar and Sven Koenig. [Multi-Agent Path Finding with Deadlines: Preliminary Results.](http:jiaoyang-li.github.io/2018-AAMAS.pdf) In <i>Proceedings of the International Joint Conference on Autonomous Agents and Multiagent Systems (AAMAS)<\i>. (in print), 2018.

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
