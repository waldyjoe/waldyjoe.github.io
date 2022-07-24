---
id: MaAAMAS17
permalink: /publications/2017-AAMAS
title: "Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks"
venue: 'International Conference on Autonomous Agents and Multi-Agent Systems'
venue-abbr: 'AAMAS'
pages: 837--845
year: 2017
pdfurl: http://jiaoyang-li.github.io/files/2017-AAMAS.pdf
publisherurl: https://dl.acm.org/citation.cfm?id=3091243
authors: Hang Ma, **Jiaoyang Li**, T. K. Satish Kumar and Sven Koenig. 
excerpt: 'This paper is about the number 3. The number 4 is left for future work.'
collection: publications
layout: archive
author_profile: true
---

{% include base_path %}

{% if page.pages %}
  {{ page.title }} <br>
  {{ page.authors }} <br>
  <i>{{ page.venue }} (<strong>{{ page.venue-abbr }}</strong>)</i>, pages {{ page.pages }}, {{ page.year }}. <br>
{% else %}
  {{ page.title }} <br>
  {{ page.authors }} <br>
  <i>{{ page.venue }} (<strong>{{ page.venue-abbr }}</strong>)</i>, (in print), {{ page.year }}. <br>
{% endif %}
% if page.publisherurl %}
  [[doi]({{ page.publisherurl }})]
{% endif %}
% if page.pdfurl %}
  [[pdf]({{ page.pdfurl }})]
{% endif %}
[<a href="javascript:void(0)" onclick="(function(target, id) {
  if ($('#' + id).css('display') == 'block') { $('#' + id).hide('fast'); $(target).text('bibtex') }
  else { $('#' + id).show('fast'); $(target).text('bibtex▲') } })(this, 'bibtex-{{ page.id }}');">bibtex</a>]
<div id="bibtex-{{ page.id }}" style="display:none">
  <pre>@inproceedings{ {{ page.id }},
    author    = {Hang Ma and Jiaoyang Li and T. K. Satish Kumar and Sven Koenig},
    title     = {Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks},
    booktitle = {Proceedings of the International Conference on Autonomous Agents and Multi-Agent Systems (AAMAS)},
    pages     = {837--845},
    year      = {2017}
  }
  </pre>
</div>


<pre>
@inproceedings{ {{ page.id }},
  author    = {Hang Ma and Jiaoyang Li and T. K. Satish Kumar and Sven Koenig},
  title     = { {{page.title}} },
  booktitle = {Proceedings of the International Conference on Autonomous Agents and Multi-Agent Systems (AAMAS)},
  pages     = { {{page.pages}} },
  year      = { {{page.year}} }
}
</pre>