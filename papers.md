---
layout: default
title: Papers & Talks
---

<div class="page-header">
  <h1>Papers &amp; Talks</h1>
</div>

<style>
  /* Common badge styles */
  .badge-custom {
    display: inline-block;
    padding: 0.15rem 0.45rem;
    font-size: 0.78rem;
    font-weight: 600;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: 4px;
    text-decoration: none !important;
    margin-left: 0.3rem;
    transition: opacity 0.15s ease-in-out;
  }
  .badge-custom:hover {
    opacity: 0.85;
  }
  
  /* Color palette optimized for color-blind accessibility */
  .badge-slides {
    background-color: #0056b3; /* High-contrast Blue */
    color: #ffffff !important;
  }
  .badge-video-link {
    background-color: #d95f02; /* Vivid Orange/Amber */
    color: #ffffff !important;
  }
</style>

<div class="section">
  <div class="section-title">Papers</div>
  <a href="https://scholar.google.com/citations?user=SC1r-GAAAAAJ&hl=ko&oi=ao" target="_blank" class="scholar-link">
    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" style="width:15px;height:15px;fill:currentColor"><path d="M12 24a7 7 0 1 1 0-14 7 7 0 0 1 0 14zm0-24L0 9.5h3.6v8.4C4.8 19.5 7.9 21 12 21s7.2-1.5 8.4-3.1V9.5H24L12 0z"/></svg>
    Google Scholar Profile
  </a>
  <p style="font-size:0.85rem;color:var(--text-light);margin-bottom:1rem;">†: (co-)1st author &nbsp;·&nbsp; *: (co-)corresponding author &nbsp;·&nbsp; Note: Where no author is designated as the first author (†), names are listed in alphabetical order by last name, as is standard practice in mathematical journals.</p>

  {% assign prep_count = site.data.papers.preprints.size %}
  {% assign pub_count = site.data.papers.published.size %}
  {% assign total_papers_count = prep_count | plus: pub_count %}

  <p style="font-size:0.95rem;font-weight:600;color:var(--text-muted);margin-bottom:0.6rem;">Preprints &amp; In Preparation</p>
  <ol class="paper-list">
    {% for paper in site.data.papers.preprints %}
    {% assign display_authors = paper.authors | replace: '[*]', '<span>*</span>' | replace: '†', '<sup>†</sup>' | markdownify | remove: '<p>' | remove: '</p>' %}
    {% assign current_num = total_papers_count | minus: forloop.index0 %}
    <li class="paper-item" value="{{ current_num }}">
      <div class="authors">{{ display_authors }}</div>
      <div class="title">
        {{ paper.title }}
        {% if paper.url_arxiv %}<a href="{{ paper.url_arxiv }}" target="_blank" class="badge badge-arxiv">arXiv</a>{% endif %}
        {% if paper.url_biorxiv %}<a href="{{ paper.url_biorxiv }}" target="_blank" class="badge badge-arxiv">bioRxiv</a>{% endif %}
        {% if paper.type == 'review' %}
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
  <ol class="paper-list">
    {% for paper in site.data.papers.published %}
    {% assign display_authors = paper.authors | replace: '[*]', '<span>*</span>' | replace: '†', '<sup>†</sup>' | markdownify | remove: '<p>' | remove: '</p>' %}
    {% assign current_num = total_papers_count | minus: prep_count | minus: forloop.index0 %}
    <li class="paper-item" value="{{ current_num }}">
      <div class="authors">{{ display_authors }}</div>
      <div class="title">
        <em>{{ paper.title }}</em>
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

<div class="section">
  <div class="section-title">Book Chapters</div>
  {% assign book_count = site.data.papers.book_chapters.size %}
  <ol class="paper-list">
    {% for chapter in site.data.papers.book_chapters %}
    {% assign display_authors = chapter.authors | replace: '[*]', '<span>*</span>' | replace: '†', '<sup>†</sup>' | markdownify | remove: '<p>' | remove: '</p>' %}
    {% assign current_book_num = book_count | minus: forloop.index0 %}
    <li class="paper-item" value="{{ current_book_num }}">
      <div class="authors">{{ display_authors }}</div>
      <div class="title">
        <em>{{ chapter.title }}</em>
        {% if chapter.url_journal %}<a href="{{ chapter.url_journal }}" target="_blank" class="badge badge-journal">Link</a>{% endif %}
      </div>
      <div class="venue">{{ chapter.venue }}</div>
    </li>
    {% endfor %}
  </ol>
</div>

<div class="section">
  <div class="section-title">Invited Talks</div>
  <p style="font-size:0.85rem;color:var(--text-light);margin-bottom:0.8rem;">SMB: Society for Mathematical Biology · KSMB: Korean SMB · SIAM: Society for Industrial and Applied Mathematics · KSIAM: Korean SIAM · KMS: Korean Mathematical Society</p>
  <ul class="talk-list">
    {% for talk in site.data.talks.invited %}
    <li class="talk-item">
      <span class="talk-date">{{ talk.date }}</span>
      <span class="talk-content">
        <span style="font-weight:500;">{{ talk.event }}</span>{% if talk.location %}, {{ talk.location }}{% endif %}
        {% if talk.url %}<a href="{{ talk.url }}" target="_blank" class="badge-custom badge-video-link">Link</a>{% endif %}
        {% if talk.extra_url %}<a href="{{ talk.extra_url }}" target="_blank" class="badge-custom badge-video-link">{{ talk.extra_label }}</a>{% endif %}
        {% if talk.slides_url %}<a href="{{ talk.slides_url }}" target="_blank" class="badge-custom badge-slides">Slides</a>{% endif %}
        {% if talk.title %}<br><span style="font-style:italic;color:var(--text-muted);font-size:0.88rem;">{{ talk.title }}</span>{% endif %}
      </span>
    </li>
    {% endfor %}
  </ul>
</div>

<div class="section">
  <div class="section-title">Contributed Talks &amp; Posters</div>
  <ul class="talk-list">
    {% for talk in site.data.talks.contributed %}
    <li class="talk-item">
      <span class="talk-date">{{ talk.date }}</span>
      <span class="talk-content">
        <span style="font-weight:500;">{{ talk.event }}</span>{% if talk.location %}, {{ talk.location }}{% endif %}
        {% if talk.type == 'poster' %} <span style="font-size:0.82rem;color:var(--text-light);">(Poster)</span>{% endif %}
        {% if talk.url %}<a href="{{ talk.url }}" target="_blank" class="badge-custom badge-video-link">Link</a>{% endif %}
        {% if talk.slides_url %}<a href="{{ talk.slides_url }}" target="_blank" class="badge-custom badge-slides">Slides</a>{% endif %}
        {% if talk.title %}<br><span style="font-style:italic;color:var(--text-muted);font-size:0.88rem;">{{ talk.title }}</span>{% endif %}
      </span>
    </li>
    {% endfor %}
  </ul>
</div>

<div class="section">
  <div class="section-title">Outreach &amp; Public Engagement</div>
  <ul class="talk-list">
    {% for item in site.data.service.outreach %}
    <li class="talk-item">
      <span class="talk-date">{{ item.date }}</span>
      <span class="talk-content">
        <span style="font-weight:500;">{{ item.title }}</span>, {{ item.venue }}
        {% if item.url %}<a href="{{ item.url }}" target="_blank" class="badge-custom badge-video-link">Link</a>{% endif %}
        {% if item.slides_url %}<a href="{{ item.slides_url }}" target="_blank" class="badge-custom badge-slides">Slides</a>{% endif %}
        {% if item.talk_title %}<br><span style="font-style:italic;color:var(--text-muted);font-size:0.88rem;">{{ item.talk_title }}</span>{% endif %}
        {% if item.note %}<br><span style="font-size:0.88rem;color:var(--text-light);">{{ item.note }}</span>{% endif %}
      </span>
    </li>
    {% endfor %}
  </ul>
</div>