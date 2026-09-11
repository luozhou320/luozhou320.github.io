---
layout: page
permalink: /awards/
title: Awards
description: Selected academic awards and honors.
nav: true
nav_order: 3
---

<ol class="awards-timeline" aria-label="Awards in reverse chronological order">
  <li class="awards-timeline__year">
    <time datetime="2026">2026</time>
    <span class="awards-timeline__marker" aria-hidden="true"></span>
    <div class="awards-timeline__entries">
      <article class="award-entry">
        <h2>Outstanding Graduate</h2>
        <p>Donghua University</p>
      </article>
      <article class="award-entry">
        <h2>Outstanding Ph.D. Thesis</h2>
        <p>Donghua University</p>
      </article>
      <article class="award-entry">
        <h2>Student Travel Grant</h2>
        <p>IEEE INFOCOM 2026</p>
      </article>
    </div>
  </li>

  <li class="awards-timeline__year">
    <time datetime="2025">2025</time>
    <span class="awards-timeline__marker" aria-hidden="true"></span>
    <div class="awards-timeline__entries">
      <article class="award-entry">
        <h2>Best Presentation in Session</h2>
        <p>IEEE ICPADS 2025</p>
      </article>
    </div>
  </li>
</ol>

<style>
  .awards-timeline {
    --timeline-year-width: 4rem;

    position: relative;
    display: grid;
    gap: 2.5rem;
    margin: 2.5rem 0 0;
    padding: 0;
    list-style: none;
  }

  .awards-timeline::before {
    position: absolute;
    top: 0.5rem;
    bottom: 0.5rem;
    left: calc(var(--timeline-year-width) + 0.75rem);
    width: 1px;
    background: var(--global-divider-color);
    content: "";
  }

  .awards-timeline__year {
    position: relative;
    display: grid;
    grid-template-columns: var(--timeline-year-width) 1.5rem minmax(0, 1fr);
    align-items: start;
  }

  .awards-timeline__year time {
    padding-top: 0.05rem;
    color: var(--global-theme-color);
    font-size: 1rem;
    font-variant-numeric: tabular-nums;
    font-weight: 700;
  }

  .awards-timeline__marker {
    z-index: 1;
    width: 0.7rem;
    height: 0.7rem;
    margin: 0.38rem auto 0;
    border: 2px solid var(--global-bg-color);
    border-radius: 50%;
    background: var(--global-theme-color);
    box-shadow: 0 0 0 1px var(--global-theme-color);
  }

  .awards-timeline__entries {
    display: grid;
    gap: 0.85rem;
  }

  .award-entry {
    padding: 1rem 1.1rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.45rem;
    background: var(--global-card-bg-color);
  }

  .award-entry h2 {
    margin: 0;
    font-size: 1.05rem;
    line-height: 1.4;
  }

  .award-entry p {
    margin: 0.3rem 0 0;
    color: var(--global-text-color-light);
    font-size: 0.9rem;
    line-height: 1.5;
  }

  @media (max-width: 575.98px) {
    .awards-timeline {
      --timeline-year-width: 0rem;

      gap: 2rem;
      margin-top: 2rem;
    }

    .awards-timeline::before {
      left: 0.75rem;
    }

    .awards-timeline__year {
      grid-template-columns: 1.5rem minmax(0, 1fr);
    }

    .awards-timeline__year time {
      grid-column: 2;
      margin-bottom: 0.7rem;
    }

    .awards-timeline__marker {
      grid-row: 1 / span 2;
    }

    .awards-timeline__entries {
      grid-column: 2;
    }
  }
</style>
