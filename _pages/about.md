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

I am currently a postdoctoral researcher in the Department of Computer Science and Engineering at [The Hong Kong University of Science and Technology (HKUST)](https://hkust.edu.hk/), working with [Prof. Qian Zhang (张黔)](https://seng.hkust.edu.hk/about/people/faculty/qian-zhang).

In 06/2026, I obtained my Ph.D. degree in Software Engineering from [Donghua University (DHU)](https://english.dhu.edu.cn/) under the supervision of [Prof. Shan Chang (常姗)](https://www.dhu.edu.cn/2021/0603/c19081a227424/pagem.htm). My research lies at the intersection of mobile and wearable computing, ubiquitous sensing, and IoT security and privacy. I am particularly interested in earable sensing, user authentication, side-channel security, and privacy-preserving intelligent systems, with an emphasis on practical sensing and interaction techniques for mobile, earable, and wearable devices. I have published 10+ papers in leading international conferences and journals, including IEEE INFOCOM, ICDCS, TMC, TDSC, IoT Journal, ACM MM, and ICASSP. My publications have received <a class="citation-badge" href="https://scholar.google.com/citations?user=3w2CkwIAAAAJ&hl=zh-CN" aria-label="View my citations on Google Scholar"><span class="citation-badge__label"><i class="fas fa-graduation-cap" aria-hidden="true"></i> citations</span><strong id="total_cit" class="citation-badge__value">—</strong></a> according to Google Scholar.

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

- *2026–Present*, **Postdoctoral Researcher**, Department of Computer Science and Engineering, The Hong Kong University of Science and Technology. Working with [Prof. Qian Zhang (张黔)](https://seng.hkust.edu.hk/about/people/faculty/qian-zhang).
- *2023*, **Visiting Scholar**, University of Electronic Science and Technology of China (UESTC), advised by [Prof. Li Lu (鲁力)](https://www.scse.uestc.edu.cn/info/1081/12001.htm). Developed an earable sensing prototype for wearable sensing and security research.
- *2020–2022*, **Mobile & IoT Systems Engineer**, Nanjing FiberHome Starry Sky Communication Co., Ltd.
- *2019–2020*, **Industrial IoT Systems Engineer**, China Aviation Industry Information Center.

<span class='anchor' id='education'></span>

# 🎓 Education

- *2022–2026*, **Ph.D. in Software Engineering**, Donghua University. Advised by Prof. Shan Chang (常姗); research focused on IoT security, mobile sensing, and computing.
- *2017–2020*, **Master's degree in Electronic and Information Engineering**, Jiangsu University of Science and Technology.
- *2013–2017*, **Bachelor's degree in Electronic and Information Engineering**, Tianjin Renai College.

<span class='anchor' id='projects'></span>

# 📌 Research Project

- *2025–2026*, **Project Lead**, Doctoral Student Innovation Fund, Donghua University. “Perception Enhancement for Wearable Devices with MEMS Sensors” (Grant No. CUSF-DH-D-2025031).
