---
layout: page
permalink: /service/
title: Services
description: Journal reviewing and academic service.
nav: true
nav_order: 4
---

<div class="services-directory">
  <section class="service-section" aria-labelledby="technical-program-committee">
    <header class="service-section__header">
      <span class="service-section__index" aria-hidden="true">01</span>
      <h2 id="technical-program-committee">Technical Program Committee</h2>
    </header>
    <p class="service-status"><span aria-hidden="true"></span>To be announced</p>
  </section>

  <section class="service-section" aria-labelledby="journal-reviewer">
    <header class="service-section__header">
      <span class="service-section__index" aria-hidden="true">02</span>
      <h2 id="journal-reviewer">Journal Reviewer</h2>
    </header>
    <ul class="service-list">
      <li>IEEE Transactions on Dependable and Secure Computing</li>
      <li>IEEE Internet of Things Journal</li>
      <li>Peer-to-Peer Networking and Applications</li>
      <li>Scientific Reports</li>
    </ul>
  </section>

  <section class="service-section" aria-labelledby="conference-reviewer">
    <header class="service-section__header">
      <span class="service-section__index" aria-hidden="true">03</span>
      <h2 id="conference-reviewer">Conference Reviewer</h2>
    </header>
    <p class="service-status"><span aria-hidden="true"></span>To be announced</p>
  </section>
</div>

<style>
  .services-directory {
    margin-top: 2.5rem;
    border-bottom: 1px solid var(--global-divider-color);
  }

  .service-section {
    display: grid;
    grid-template-columns: minmax(14rem, 0.85fr) minmax(0, 1.6fr);
    gap: 2.5rem;
    padding: 1.8rem 0;
    border-top: 1px solid var(--global-divider-color);
  }

  .service-section__header {
    display: grid;
    grid-template-columns: 2rem minmax(0, 1fr);
    gap: 0.75rem;
    align-items: baseline;
  }

  .service-section__index {
    color: var(--global-theme-color);
    font-size: 0.8rem;
    font-variant-numeric: tabular-nums;
    font-weight: 700;
    letter-spacing: 0.08em;
  }

  .service-section h2 {
    margin: 0;
    font-size: 1.15rem;
    line-height: 1.45;
  }

  .service-list {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.9rem 2rem;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .service-list li {
    position: relative;
    margin: 0;
    padding-left: 1rem;
    line-height: 1.55;
  }

  .service-list li::before {
    position: absolute;
    top: 0.65em;
    left: 0;
    width: 0.35rem;
    height: 0.35rem;
    border-radius: 50%;
    background: var(--global-theme-color);
    content: "";
  }

  .service-status {
    display: inline-flex;
    gap: 0.6rem;
    align-items: center;
    width: fit-content;
    margin: 0;
    color: var(--global-text-color-light);
    font-size: 0.95rem;
    line-height: 1.5;
  }

  .service-status span {
    width: 0.45rem;
    height: 0.45rem;
    border: 1px solid var(--global-text-color-light);
    border-radius: 50%;
  }

  @media (max-width: 767.98px) {
    .services-directory {
      margin-top: 2rem;
    }

    .service-section {
      grid-template-columns: 1fr;
      gap: 1rem;
      padding: 1.5rem 0;
    }

    .service-list {
      grid-template-columns: 1fr;
      gap: 0.8rem;
      padding-left: 2.75rem;
    }

    .service-status {
      margin-left: 2.75rem;
    }
  }
</style>
