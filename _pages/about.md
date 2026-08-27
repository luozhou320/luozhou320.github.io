---
permalink: /
title: ""
excerpt: "Luo Zhou is a Postdoctoral Researcher at HKUST."
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<span class='anchor' id='about-me'></span>

# About Me

I am currently a postdoctoral researcher in the Department of Computer Science and Engineering at [The Hong Kong University of Science and Technology (HKUST)](https://cse.hkust.edu.hk/), working with [Prof. Qian Zhang](https://seng.hkust.edu.hk/about/people/faculty/qian-zhang).

In 2026, I received my Ph.D. in Software Engineering from Donghua University under the supervision of [Prof. Shan Chang](https://www.dhu.edu.cn/2021/0603/c19081a227424/pagem.htm). My research lies at the intersection of mobile and wearable computing, ubiquitous sensing, and IoT security and privacy. I am particularly interested in earable sensing, user authentication, side-channel security, and privacy-preserving intelligent systems, with an emphasis on practical sensing and interaction techniques for mobile, earable, and wearable devices.

<!-- <span class='anchor' id='research'></span>

My research lies at the intersection of mobile and wearable computing, ubiquitous sensing, and IoT security and privacy. I am particularly interested in earable sensing, user authentication, side-channel security, and privacy-preserving intelligent systems, with an emphasis on practical sensing and interaction techniques for mobile, earable, and wearable devices.

<span class='anchor' id='news'></span> -->

# 🔥 News

- *2026*: **Baro2Talk** was published at IEEE INFOCOM 2026.
- *2026*: **Speak and Be Known** was published in IEEE Transactions on Mobile Computing.
- *2026*: **AirSpy** was published in IEEE Transactions on Consumer Electronics.
- *2025*: **BaroAuth** was published at IEEE ICDCS 2025.

<span class='anchor' id='publications'></span>

# 📝 Publications

<p class="publications-intro">A complete list of my published and accepted work. For the latest citation data, please visit my <a href="https://scholar.google.com/citations?user=3w2CkwIAAAAJ&hl=zh-CN">Google Scholar profile</a>. Total citations: <strong><span id="total_cit">see Google Scholar</span></strong>.</p>

{% assign current_publication_year = "" %}
{% for publication in site.data.publications %}
{% capture publication_year %}{{ publication.year }}{% endcapture %}
{% if publication_year != current_publication_year %}
<h2 class="publication-year">{{ publication.year }}</h2>
{% assign current_publication_year = publication_year %}
{% endif %}
{% include publication-card.html publication=publication %}
{% endfor %}

<span class='anchor' id='experience'></span>

# 💼 Experience

- *2026–Present*, **Postdoctoral Researcher**, Department of Computer Science and Engineering, The Hong Kong University of Science and Technology. Working with Prof. Qian Zhang.
- *2023*, **Visiting Scholar**, University of Electronic Science and Technology of China. Developed an earable sensing prototype for wearable sensing and security research.
- *2020–2022*, **Mobile & IoT Systems Engineer**, Nanjing FiberHome Starry Sky Communication Co., Ltd.
- *2019–2020*, **Industrial IoT Systems Engineer**, China Aviation Industry Information Center.

<span class='anchor' id='education'></span>

# 🎓 Education

- *2022–2026*, **Ph.D. in Software Engineering**, Donghua University. Advised by Prof. Shan Chang; research focused on IoT security, mobile sensing, and computing.
- *2017–2020*, **Master's degree in Electronic and Information Engineering**, Jiangsu University of Science and Technology.
- *2013–2017*, **Bachelor's degree in Electronic and Information Engineering**, Tianjin Renai College.

<span class='anchor' id='projects'></span>

# 📌 Research Project

- *2025–2026*, **Project Lead**, Doctoral Student Innovation Fund, Donghua University. “Perception Enhancement for Wearable Devices with MEMS Sensors” (Grant No. CUSF-DH-D-2025031).
