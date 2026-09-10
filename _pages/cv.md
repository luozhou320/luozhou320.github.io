---
layout: default
permalink: /cv/
title: CV
nav: true
nav_order: 5
cv_pdf: /assets/pdf/Luo_Zhou_CV.pdf
cv_format: rendercv
description: Academic background, professional experience, and research projects.
toc:
  sidebar: left
---

<link rel="stylesheet" href="{{ '/assets/css/al-folio-cv.css' | relative_url | bust_file_cache }}">

{% al_folio_cv_render %}

<style>
  .cv .list-group,
  .cv .list-group-item {
    padding-left: 0;
    list-style: none;
  }

  .cv .list-group-item::marker {
    content: "";
  }

  .cv .date-column {
    transform: none;
  }

  .cv .date-column > .table-cv {
    width: 100%;
    margin-inline: auto;
  }
</style>
