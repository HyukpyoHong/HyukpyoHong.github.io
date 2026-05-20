---
layout: default
title: Papers & Talks
---

<div class="page-header">
  <h1>Papers &amp; Talks</h1>
</div>

<!-- PAPERS -->
<div class="section">
  <div class="section-title">Papers</div>
  <a href="https://scholar.google.com/citations?user=SC1r-GAAAAAJ&hl=ko&oi=ao" target="_blank" class="scholar-link">
    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" style="width:15px;height:15px;fill:currentColor"><path d="M12 24a7 7 0 1 1 0-14 7 7 0 0 1 0 14zm0-24L0 9.5h3.6v8.4C4.8 19.5 7.9 21 12 21s7.2-1.5 8.4-3.1V9.5H24L12 0z"/></svg>
    Google Scholar Profile
  </a>
  <p style="font-size:0.85rem;color:var(--text-light);margin-bottom:1rem;">†: (co-)1st author &nbsp;·&nbsp; *: (co-)corresponding author &nbsp;·&nbsp; Note: Where no author is designated as the first author (†), names are listed in alphabetical order by last name, as is standard practice in mathematical journals.</p>

  <p style="font-size:0.95rem;font-weight:600;color:var(--text-muted);margin-bottom:0.6rem;">Preprints &amp; In Preparation</p>
  <ol class="paper-list" start="1">
    {% for paper in site.data.papers.preprints %}
    {% assign display_authors = paper.authors | replace: '[*]', '*' | replace: '†', '<sup>†</sup>' | markdownify | remove: '<p>' | remove: '</p>' %}
    <li class="paper-item">
      <div class="authors">{{ display_authors }}</div>
      <div class="title">
        {{ paper.title }}
        {% if paper.type == 'review' %}
          {% if paper.url_arxiv %}<a href="{{ paper.url_arxiv }}" target="_blank" class="badge badge-arxiv">arXiv</a>{% endif %}
          <span class="badge badge-preprint">Under Review</span>
        {% elsif paper.type == 'submitted' %}
          <span class="badge badge-preprint">Submitted</span>
        {% else %}
          <span class="badge badge-preprint">In Prep</span>
        {% endif %}
      </div>
    </li>
    {% endfor %}
  </ol>

  <p style="font-size:0.95rem;font-weight:600;color:var(--text-muted);margin-bottom:0.6rem;margin-top:1.5rem;">Published &amp; Accepted</p>
  <ol class="paper-list" start="1">
    {% for paper in site.data.papers.published %}
    {% assign display_authors = paper.authors | replace: '[*]', '*' | replace: '†', '<sup>†</sup>' | markdownify | remove: '<p>' | remove: '</p>' %}
    <li class="paper-item">
      <div class="authors">{{ display_authors }}</div>
      <div class="title">
        {{ paper.title }}
        {% if paper.url_arxiv %}<a href="{{ paper.url_arxiv }}" target="_blank" class="badge badge-arxiv">arXiv</a>{% endif %}
        {% if paper.url_biorxiv %}<a href="{{ paper.url_biorxiv }}" target="_blank" class="badge badge-arxiv">bioRxiv</a>{% endif %}
        {% if paper.url_medrxiv %}<a href="{{ paper.url_medrxiv }}" target="_blank" class="badge badge-arxiv">medRxiv</a>{% endif %}
        {% if paper.url_journal %}<a href="{{ paper.url_journal }}" target="_blank" class="badge badge-journal">Journal</a>{% endif %}
      </div>
      <div class="venue"><em>{{ paper.venue }}</em>, {{ paper.year }}</div>
    </li>
    {% endfor %}
  </ol>
</div>

<!-- BOOK CHAPTERS -->
<div class="section">
  <div class="section-title">Book Chapters</div>
  <ol class="paper-list" start="1">
    {% for chapter in site.data.papers.book_chapters %}
    {% assign display_authors = chapter.authors | replace: '[*]', '*' | replace: '†', '<sup>†</sup>' | markdownify | remove: '<p>' | remove: '</p>' %}
    <li class="paper-item">
      <div class="authors">{{ display_authors }}</div>
      <div class="title">
        {{ chapter.title }}
        {% if chapter.url_journal %}<a href="{{ chapter.url_journal }}" target="_blank" class="badge badge-journal">Link</a>{% endif %}
      </div>
      <div class="venue">{{ chapter.venue }}</div>
    </li>
    {% endfor %}
  </ol>
</div>

<!-- INVITED TALKS -->
<div class="section">
  <div class="section-title">Invited Talks</div>
  <p style="font-size:0.85rem;color:var(--text-light);margin-bottom:0.8rem;">SMB: Society for Mathematical Biology · KSMB: Korean SMB · SIAM: Society for Industrial and Applied Mathematics · KSIAM: Korean SIAM · KMS: Korean Mathematical Society</p>
  <ul class="talk-list">
    {% for talk in site.data.talks.invited %}
    <li class="talk-item">
      <span class="talk-date">{{ talk.date }}</span>
      <span class="talk-content">
        <span style="font-weight:500;">{{ talk.event }}</span>{% if talk.location %}, {{ talk.location }}{% endif %}
        {% if talk.url %} — <a href="{{ talk.url }}" target="_blank">link</a>{% endif %}
        {% if talk.extra_url %} · <a href="{{ talk.extra_url }}" target="_blank">{{ talk.extra_label }}</a>{% endif %}
        {% if talk.title %}<br><span style="font-style:italic;color:var(--text-muted);font-size:0.88rem;">{{ talk.title }}</span>{% endif %}
      </span>
    </li>
    {% endfor %}
  </ul>
</div>

<!-- CONTRIBUTED TALKS & POSTERS -->
<div class="section">
  <div class="section-title">Contributed Talks &amp; Posters</div>
  <ul class="talk-list">
    {% for talk in site.data.talks.contributed %}
    <li class="talk-item">
      <span class="talk-date">{{ talk.date }}</span>
      <span class="talk-content">
        <span style="font-weight:500;">{{ talk.event }}</span>{% if talk.location %}, {{ talk.location }}{% endif %}
        {% if talk.type == 'poster' %} <span style="font-size:0.82rem;color:var(--text-light);">(Poster)</span>{% endif %}
        {% if talk.url %} — <a href="{{ talk.url }}" target="_blank">link</a>{% endif %}
        {% if talk.title %}<br><span style="font-style:italic;color:var(--text-muted);font-size:0.88rem;">{{ talk.title }}</span>{% endif %}
      </span>
    </li>
    {% endfor %}
  </ul>
</div>
