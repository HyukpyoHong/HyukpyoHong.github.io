---
layout: default
title: Teaching
---

<div class="page-header">
  <h1>Teaching &amp; Mentoring</h1>
</div>

<!-- TEACHING -->
<div class="section">
  <div class="section-title">Teaching</div>

  {% if site.data.teaching.award %}
  <div class="award-badge">{{ site.data.teaching.award }}</div>
  {% endif %}

  {% assign uw = site.data.teaching.courses | where: "institution", "UW–Madison" %}
  {% assign kaist = site.data.teaching.courses | where: "institution", "KAIST" %}

  <div class="teaching-block">
    <h3>UW–Madison</h3>
    <ul class="course-list">
      {% for course in uw %}
      <li class="course-item">
        <span class="course-year">{{ course.term }}</span>
        <span>[{{ course.role }}] {{ course.course }}</span>
      </li>
      {% endfor %}
    </ul>
  </div>

  <div class="teaching-block">
    <h3>KAIST</h3>
    <ul class="course-list">
      {% for course in kaist %}
      <li class="course-item">
        <span class="course-year">{{ course.term }}</span>
        <span>[{{ course.role }}] {{ course.course }}</span>
      </li>
      {% endfor %}
    </ul>
  </div>
</div>

<!-- MENTORING -->
<div class="section">
  <div class="section-title">Mentoring</div>

  {% assign uw_mentoring = site.data.teaching.mentoring | where: "institution", "UW–Madison" %}
  {% assign kaist_mentoring = site.data.teaching.mentoring | where: "institution", "KAIST" %}

  <div class="teaching-block">
    <h3>UW–Madison</h3>
    <ul class="course-list">
      {% for m in uw_mentoring %}
      <li class="course-item" style="flex-direction:column;gap:0.2rem;">
        <span style="display:flex;gap:1rem;">
          <span class="course-year">{{ m.period }}</span>
          <span>{{ m.name }}, {{ m.description }}</span>
        </span>
        <span style="color:var(--text-muted);font-size:0.9rem;">{{ m.note }}</span>
      </li>
      {% endfor %}
    </ul>
  </div>

  <div class="teaching-block">
    <h3>KAIST</h3>
    <ul class="course-list">
      {% for m in kaist_mentoring %}
      <li class="course-item" style="flex-direction:column;gap:0.2rem;">
        <span style="display:flex;gap:1rem;">
          <span class="course-year">{{ m.period }}</span>
          <span>{{ m.name }}, {{ m.description }}</span>
        </span>
        <span style="color:var(--text-muted);font-size:0.9rem;">{{ m.note }}</span>
      </li>
      {% endfor %}
    </ul>
  </div>
</div>

<!-- TEACHING PHILOSOPHY -->
<div class="section">
  <div class="section-title">Teaching Philosophy</div>
  <div class="bio-text" style="margin-bottom:1rem;">
    <p>As a mathematician, I would like to share the beauty of mathematics with others, and as an applied mathematician, I would like to teach how useful mathematics is for solving real-world problems.</p>
  </div>
  <div class="philosophy-item">
    <p><strong>Giving a motivating example before a formal statement.</strong> One important lesson from my Ph.D. journey is to show a motivating or intuitive example before presenting a formal statement. For instance, when teaching SVD, I first demonstrate image compression to motivate the audience. Similarly, when introducing non-Markovian systems: "If tomorrow's weather depends only on today's weather, it would be easier to forecast than when it depends on the past few days." This makes audiences appreciate the challenge before we formalize it.</p>
  </div>
  <div class="philosophy-item" style="margin-top:1rem;">
    <p><strong>"No such thing as a stupid question."</strong> I always encourage students at the start of the first class: "Please don't hesitate to ask questions. You may feel like you are the only one who doesn't know the answer — but that is never true. Your questions can slow down the lecture in a meaningful way." This has consistently helped students feel comfortable visiting office hours.</p>
  </div>
</div>
