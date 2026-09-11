---
layout: default
title: About
permalink: /

profile:
  image: prof_pic.jpg
  image_circular: false
  local_name: 周骆
  role: Postdoctoral Researcher
  organization: CSE · HKUST
  location: Hong Kong, China
  origins:
    - Born in Zhenjiang, Jiangsu

biography: |
  I am a postdoctoral researcher in the Department of Computer Science and Engineering at [The Hong Kong University of Science and Technology (HKUST)](https://hkust.edu.hk/), where I work with [Prof. Qian Zhang (张黔)](https://seng.hkust.edu.hk/about/people/faculty/qian-zhang). My research investigates how subtle physical signals generated during human–device interaction can enable new sensing capabilities—and how those same signals may expose users to security and privacy risks.

  My work spans mobile and wearable computing, ubiquitous sensing, and IoT security and privacy, with particular interests in earable sensing, user authentication, side-channel security, and privacy-preserving intelligent systems. By combining sensing, signal processing, and system security, I aim to develop practical systems that are both useful and trustworthy. I have published more than ten papers in venues including IEEE INFOCOM, ICDCS, ICASSP, TMC, TDSC, IoT Journal, and ACM MM. A complete publication record and current citation metrics are available on my [Google Scholar profile](https://scholar.google.com/citations?user=3w2CkwIAAAAJ&hl=en).

  I received my Ph.D. in Software Engineering from [Donghua University (DHU)](https://english.dhu.edu.cn/) in June 2026 under the supervision of [Prof. Shan Chang (常姗)](https://www.dhu.edu.cn/2021/0603/c19081a227424/pagem.htm). In 2023, I was a visiting scholar at the University of Electronic Science and Technology of China, where I worked with [Prof. Li Lu (鲁力)](https://www.scse.uestc.edu.cn/info/1081/12001.htm) on earable sensing systems. Before beginning my doctoral studies, I worked as an engineer on mobile and industrial IoT systems. This industry experience continues to shape my emphasis on practical and deployable research. During my doctoral training, I was recognized as a DHU Outstanding Graduate, and my dissertation received the DHU Outstanding Ph.D. Thesis award.
---

<link rel="stylesheet" href="{{ '/assets/css/publication-list.css' | relative_url }}?v={{ site.time | date: '%s' }}">
<link rel="stylesheet" href="{{ '/assets/css/publication-preview.css' | relative_url }}?v={{ site.time | date: '%s' }}">

<div class="post about-page">
  <article>
    <div class="about-layout">
      <aside class="profile-panel" aria-label="Profile">
        {% assign profile_image_path = page.profile.image | prepend: 'assets/img/' %}
        {% if page.profile.image_circular %}
          {% assign profile_image_class = 'img-fluid z-depth-1 rounded-circle' %}
        {% else %}
          {% assign profile_image_class = 'img-fluid z-depth-1 rounded' %}
        {% endif %}
        {% capture profile_sizes %}(min-width: {{ site.max_width }}) 175px, (min-width: 768px) 18vw, 70vw{% endcapture %}
        {%
          include figure.liquid loading="eager" path=profile_image_path class=profile_image_class sizes=profile_sizes alt=page.profile.image
          cache_bust=true
        %}

        <div class="profile-identity">
          <div class="profile-name">{{ site.title }} ({{ page.profile.local_name }})</div>
          <div class="profile-role">{{ page.profile.role }}</div>
          <div class="profile-organization">{{ page.profile.organization }}</div>
          <div class="profile-location">{{ page.profile.location }}</div>
          <div class="profile-origins">
            {% for origin in page.profile.origins %}<span>{{ origin }}</span>{% endfor %}
          </div>
        </div>

        <div class="profile-social social" aria-label="Academic and social profiles">
          <div class="contact-icons">{% social_links %}</div>
        </div>
      </aside>

      <div class="about-main">
        <section class="about-biography" aria-labelledby="biography-heading">
          <h1 id="biography-heading">Biography</h1>
          {{ page.biography | markdownify }}
        </section>

        <section class="about-section" aria-labelledby="news-heading">
          <h2 id="news-heading">News</h2>
          <div class="news-timeline" aria-label="Recent news">
            <div class="news-entry">
              <time datetime="2026-07">07/2026</time>
              <p>I accept an offer to join the Department of Computer Science and Engineering at HKUST as a Postdoctoral Fellow.</p>
            </div>
            <div class="news-entry">
              <time datetime="2026-07">07/2026</time>
              <p>Our paper <strong>MAGIC</strong> on PPG-to-ECG translation is accepted for publication in IEEE Journal of Biomedical and Health Informatics.</p>
            </div>
            <div class="news-entry">
              <time datetime="2026-06">06/2026</time>
              <p>I receive my Ph.D. degree from Donghua University.</p>
            </div>
            <div class="news-entry">
              <time datetime="2026-04">04/2026</time>
              <p>I am awarded a Student Travel Grant to attend IEEE INFOCOM 2026.</p>
            </div>
          </div>

          <details class="earlier-news">
            <summary>Earlier news</summary>
            <div class="news-timeline" aria-label="Earlier news">
              <div class="news-entry">
                <time datetime="2026-02">02/2026</time>
                <p>Our paper on VR air-pinch keystroke inference is accepted for publication in IEEE Transactions on Consumer Electronics.</p>
              </div>
              <div class="news-entry">
                <time datetime="2026-02">02/2026</time>
                <p><strong>Speak and Be Known</strong>, an extension of <strong>BaroAuth</strong>, is accepted for publication in IEEE Transactions on Mobile Computing.</p>
              </div>
              <div class="news-entry">
                <time datetime="2025-12">12/2025</time>
                <p>Our paper <strong>Baro2Talk</strong> on voice-free communication using in-ear pressure sensing is accepted at IEEE INFOCOM 2026.</p>
              </div>
              <div class="news-entry">
                <time datetime="2025-10">10/2025</time>
                <p>Our paper <strong>Aclipse</strong> on privacy-preserving speech emotion recognition is accepted at IEEE ICPADS 2025.</p>
              </div>
              <div class="news-entry">
                <time datetime="2025-03">03/2025</time>
                <p>Our paper <strong>BaroAuth</strong> on speaking user authentication with earable devices is accepted at IEEE ICDCS 2025.</p>
              </div>
              <div class="news-entry">
                <time datetime="2024-07">07/2024</time>
                <p>Our paper on closed-box attacks against 3D face recognition systems is accepted at ACM Multimedia 2024.</p>
              </div>
              <div class="news-entry">
                <time datetime="2024-06">06/2024</time>
                <p>The extension of <strong>VOGUE</strong> is accepted for publication in IEEE Transactions on Dependable and Secure Computing.</p>
              </div>
              <div class="news-entry">
                <time datetime="2024-05">05/2024</time>
                <p>Our extended paper on physical adversarial attacks is accepted for publication in IEEE Internet of Things Journal.</p>
              </div>
              <div class="news-entry">
                <time datetime="2023-03">03/2023</time>
                <p>Our paper on physical adversarial attacks against autonomous driving systems is accepted at IEEE ICASSP 2023.</p>
              </div>
            </div>
          </details>
        </section>

        <section class="about-section" aria-labelledby="selected-publications-heading">
          <h2 id="selected-publications-heading">
            <a href="{{ '/publications/' | relative_url }}" style="color: inherit">Selected Publications</a>
          </h2>
          {% include selected_papers.liquid %}
        </section>
      </div>
    </div>

  </article>
</div>

<style>
  .about-layout {
    --profile-width: 175px;
    --profile-gap: clamp(2rem, 5vw, 4rem);
    --section-gap: clamp(2.5rem, 5vw, 3rem);

    display: grid;
    grid-template-columns: var(--profile-width) minmax(0, 1fr);
    gap: var(--profile-gap);
    align-items: start;
  }

  .profile-panel {
    text-align: center;
  }

  .profile-panel figure,
  .profile-panel picture,
  .profile-panel img {
    width: 100%;
    margin: 0;
  }

  .profile-identity {
    margin-top: 1.25rem;
  }

  .profile-name {
    font-size: 1.45rem;
    font-weight: 400;
    line-height: 1.3;
  }

  .profile-role {
    margin-top: 0.45rem;
    color: var(--global-text-color-light);
  }

  .profile-organization,
  .profile-location {
    margin-top: 0.3rem;
    font-size: 0.95rem;
  }

  .profile-origins {
    display: grid;
    gap: 0.2rem;
    margin-top: 0.8rem;
    color: var(--global-text-color-light);
    font-size: 0.82rem;
    line-height: 1.45;
  }

  .profile-social {
    margin-top: 1.1rem;
  }

  .profile-social .contact-icons {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.7rem;
    font-size: 1.55rem;
  }

  .profile-social .contact-icons a,
  .profile-social .contact-icons svg,
  .profile-social .contact-icons img {
    margin: 0;
  }

  .about-main {
    min-width: 0;
  }

  .about-biography h1 {
    margin-top: -0.15rem;
    margin-bottom: 1.25rem;
  }

  .about-biography p {
    margin-bottom: 1.15rem;
    hyphens: auto;
    line-height: 1.75;
    text-align: justify;
    text-justify: inter-word;
  }

  .about-main > section + section {
    margin-top: var(--section-gap);
  }

  .about-main section > :last-child {
    margin-bottom: 0;
  }

  .about-main .about-section > h2 {
    margin-top: 0;
  }

  .news-timeline {
    position: relative;
    display: grid;
    gap: 0.9rem;
    margin-top: 1rem;
    padding-left: 1.25rem;
  }

  .news-timeline::before {
    position: absolute;
    top: 0.35rem;
    bottom: 0.35rem;
    left: 0.25rem;
    width: 1px;
    background: var(--global-divider-color);
    content: "";
  }

  .news-entry {
    position: relative;
    display: grid;
    grid-template-columns: 4.25rem minmax(0, 1fr);
    gap: 0.75rem;
    align-items: start;
  }

  .news-entry::before {
    position: absolute;
    top: 0.45rem;
    left: -1.25rem;
    width: 0.55rem;
    height: 0.55rem;
    border: 2px solid var(--global-bg-color);
    border-radius: 50%;
    background: var(--global-theme-color);
    content: "";
  }

  .news-entry time {
    padding-top: 0.12rem;
    color: var(--global-text-color-light);
    font-variant-numeric: tabular-nums;
    font-weight: 600;
  }

  .news-entry p {
    margin: 0;
    hyphens: auto;
    line-height: 1.6;
    text-align: justify;
    text-justify: inter-word;
  }

  .earlier-news {
    margin-top: 1.25rem;
  }

  .earlier-news summary {
    display: inline-flex;
    min-height: 2.75rem;
    align-items: center;
    padding: 0.35rem 0.75rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.2rem;
    color: var(--global-text-color-light);
    cursor: pointer;
    font-size: 0.9rem;
    list-style: none;
    transition:
      border-color 0.15s ease,
      color 0.15s ease;
  }

  .earlier-news summary:hover {
    border-color: var(--global-theme-color);
    color: var(--global-theme-color);
  }

  .earlier-news summary:focus-visible {
    outline: 2px solid var(--global-theme-color);
    outline-offset: 3px;
  }

  .earlier-news summary::-webkit-details-marker {
    display: none;
  }

  .earlier-news summary::after {
    margin-left: 0.55rem;
    content: "+";
  }

  .earlier-news[open] summary::after {
    content: "−";
  }

  .earlier-news[open] .news-timeline {
    margin-top: 1rem;
  }

  @media (max-width: 767.98px) {
    .about-layout {
      grid-template-columns: minmax(0, 1fr);
      gap: 2.25rem;
    }

    .profile-panel {
      width: min(100%, 182px);
      margin: 0 auto;
    }

    .about-biography h1 {
      text-align: center;
    }

    .about-biography p,
    .news-entry p {
      hyphens: manual;
      text-align: left;
    }

  }
</style>

<script defer src="{{ '/assets/js/publication-preview.js' | relative_url | bust_file_cache }}"></script>
<script defer src="{{ '/assets/js/profile-email.js' | relative_url }}"></script>
