---
layout: page
permalink: /publications/
title: Publications
description: A complete list of published and accepted work.
nav: true
nav_order: 2
---

<link rel="stylesheet" href="{{ '/assets/css/publication-list.css' | relative_url }}?v={{ site.time | date: '%s' }}">
<link rel="stylesheet" href="{{ '/assets/css/publication-preview.css' | relative_url }}?v={{ site.time | date: '%s' }}">

{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>

<script defer src="{{ '/assets/js/publication-preview.js' | relative_url | bust_file_cache }}"></script>
