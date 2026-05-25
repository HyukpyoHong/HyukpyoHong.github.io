---
layout: default
title: Research
---

<!--
  Collaborator links (commented out — for reference only):
  Hanbaek Lyu: https://hanbaeklyu.com/
  Qin Li: https://people.math.wisc.edu/~qli36/
  Matthew Colbrook: https://www.damtp.cam.ac.uk/user/mjc249/home.html
  Seewoo Lee: https://seewoo5.github.io
  Dae Wook Kim: https://sites.google.com/view/dae-wook-kim/home
  Jinsu Kim: https://mathjinsukim.com
  Gheorghe Craciun: https://people.math.wisc.edu/~craciun/
  Diego Rojas La Luz: https://sites.google.com/wisc.edu/diego-rojas-la-luz/
  Yuji Hirono: https://sites.google.com/site/yujihironooo/
  Wolfram Liebermeister: https://wolfram-liebermeister.pages-forge.inrae.fr/web/
  Jae Kyoung Kim: https://mathsci.kaist.ac.kr/~jaekkim/
  Boseung Choi: http://nslab.korea.ac.kr/
  Kresimir Josic: https://math.uh.edu/~josic/
  Hyeontae Jo: https://sites.google.com/view/hyeontae-site/
  Hyun Woong Roh: https://sites.google.com/ajou.ac.kr/ineuva-labs/
  Eun Young Kim: https://keyclocklab.wixsite.com/keyclock
  Won Chang: https://www.wonchang.net
  Hang J. Kim: https://homepages.uc.edu/~kim3h4/
  Yun Min Song: https://sites.google.com/view/yun-min-song/home
  Eui-Cheol Shin: https://pure.kaist.ac.kr/en/persons/eui-cheol-shin/
  Ji Yun Noh: https://scholarworks.korea.ac.kr/kumedicine/researcher-profile?ep=180
-->

<style>
/* ── Research page styles ───────────────────────── */
.research-overview {
  font-size: 0.97rem;
  line-height: 1.8;
  color: var(--text-muted);
  margin-bottom: 2.5rem;
}
.research-overview strong { color: var(--text); }
.research-overview a { color: var(--accent); text-decoration: none; }
.research-overview a:hover { text-decoration: underline; }
.research-overview ul {
  margin: 0.6rem 0 0.8rem 1.2rem;
  padding: 0;
}
.research-overview li { margin-bottom: 0.3rem; }

/* Big topic block */
.topic-group {
  margin-bottom: 2rem;
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
}
.topic-group-header {
  background: var(--bg-soft);
  padding: 1rem 1.4rem;
  font-size: 1rem;
  font-weight: 700;
  color: var(--text);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.topic-group-header .topic-icon {
  font-size: 1.1rem;
}

/* Accordion item */
.accordion-item {
  border-bottom: 1px solid var(--border);
}
.accordion-item:last-child { border-bottom: none; }

.accordion-trigger {
  width: 100%;
  background: none;
  border: none;
  padding: 0.85rem 1.4rem;
  text-align: left;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text);
  transition: background 0.15s;
}
.accordion-trigger:hover { background: var(--bg-soft); }
.accordion-trigger .chevron {
  flex-shrink: 0;
  width: 18px; height: 18px;
  transition: transform 0.25s ease;
  color: var(--text-light);
}
.accordion-trigger[aria-expanded="true"] .chevron {
  transform: rotate(180deg);
}
.accordion-trigger[aria-expanded="true"] {
  color: var(--accent);
  background: var(--bg-soft);
}

/* Accordion content */
.accordion-content {
  display: none;
  padding: 0 1.4rem 1.2rem;
  animation: fadeSlideIn 0.2s ease;
}
.accordion-content.open { display: block; }

@keyframes fadeSlideIn {
  from { opacity: 0; transform: translateY(-6px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Inner layout: image + text */
.topic-inner {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.2rem;
  padding-top: 0.4rem;
}
.topic-inner.has-image {
  grid-template-columns: minmax(160px, 220px) 1fr;
  align-items: start;
}
.topic-image {
  width: 100%;
  aspect-ratio: 1 / 1;
  object-fit: cover;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: var(--bg-soft);
}
.topic-text {
  font-size: 0.93rem;
  line-height: 1.75;
  color: var(--text-muted);
}
.topic-text p + p { margin-top: 0.6rem; }
.topic-text a { color: var(--accent); text-decoration: none; }
.topic-text a:hover { text-decoration: underline; }
.topic-text em { font-style: italic; }

/* Collaborators */
.collaborators {
  margin-top: 0.8rem;
  font-size: 0.86rem;
  color: var(--text-light);
}
.collaborators strong { color: var(--text-muted); font-weight: 600; }
.collaborators a { color: var(--accent); text-decoration: none; }
.collaborators a:hover { text-decoration: underline; }

/* Standalone section (no accordion) */
.topic-standalone {
  padding: 1rem 1.4rem 1.2rem;
  font-size: 0.93rem;
  line-height: 1.75;
  color: var(--text-muted);
}
.topic-standalone blockquote {
  border-left: 3px solid var(--border);
  margin: 0.6rem 0;
  padding-left: 1rem;
  font-style: italic;
  color: var(--text-light);
}

/* Mobile */
@media (max-width: 640px) {
  .topic-inner.has-image {
    grid-template-columns: 1fr;
  }
  .topic-image { max-width: 200px; }
}
</style>

<!-- ── Page header ─────────────────────────────── -->
<div class="page-header">
  <h1>Research</h1>
</div>

<!-- ── Social links ────────────────────────────── -->
<div class="social-links" style="margin-bottom:1.8rem;">
  <a href="https://scholar.google.com/citations?user=SC1r-GAAAAAJ&hl=ko&oi=ao" target="_blank" class="social-link">
    <svg viewBox="0 0 24 24" style="width:14px;height:14px;fill:currentColor"><path d="M12 24a7 7 0 1 1 0-14 7 7 0 0 1 0 14zm0-24L0 9.5h3.6v8.4C4.8 19.5 7.9 21 12 21s7.2-1.5 8.4-3.1V9.5H24L12 0z"/></svg>
    Google Scholar
  </a>
  <a href="https://github.com/HyukpyoHong" target="_blank" class="social-link">
    <svg viewBox="0 0 24 24" style="width:14px;height:14px;fill:currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
    GitHub
  </a>
</div>

<!-- ── Overview ────────────────────────────────── -->
<div class="research-overview">
  <p>My research sits at the intersection of <strong>applied mathematics (dynamical systems, mathematical biology) </strong> and <strong>scientific machine learning (sciML)</strong>. I develop mathematical and statistical tools to understand complex systems from intracellular biochemical networks to human-scale epidemics. Central questions I pursue include:</p>
  <ul>
    <li>How can nonlinear dynamical systems be represented in a computationally tractable way?</li>
    <li>How do biological systems maintain robust function despite fluctuating conditions?</li>
    <li>How can we accurately infer parameters of models with realistic, non-Markovian assumptions?</li>
  </ul>
  <p>The techniques I develop and apply span <strong>Koopman operator theory</strong>, <strong>chemical reaction network theory</strong>, <strong>Bayesian inference</strong>, <strong>stochastic processes</strong>, and <strong>machine learning</strong>. I also enjoy problem-driven collaboration with biologists and clinicians.</p>
</div>

<!-- ════════════════════════════════════════════════
     TOPIC GROUP 1 — Koopman Operator Theory
════════════════════════════════════════════════ -->
<div class="topic-group">
  <div class="topic-group-header">
    <!-- <span class="topic-icon">⚙️</span> -->
    I. Koopman Operator Theory
  </div>

  <!-- 1-1 -->
  <div class="accordion-item">
    <button class="accordion-trigger" aria-expanded="false">
      Principled Dictionary Learning via EDMD and PageRank
      <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </button>
    <div class="accordion-content">
      <div class="topic-inner">
        <!-- image placeholder: <img src="{{ '/images/research/koopman_edmd.png' | relative_url }}" class="topic-image" alt="EDMD illustration"> -->
        <div class="topic-text">
          <p>The Extended Dynamic Mode Decomposition (EDMD) approximates the Koopman operator using a finite dictionary of observable functions. A central challenge is choosing this dictionary in a principled way. I am developing an algorithm based on <em>Personalized PageRank</em> that systematically constructs and refines dictionaries, providing provable approximation guarantees for the finite-dimensional Koopman representation.</p>
          <!-- <div class="collaborators">
            <strong>Collaborators:</strong>
            <a href="https://hanbaeklyu.com/" target="_blank">Hanbaek Lyu</a>,
            <a href="https://people.math.wisc.edu/~qli36/" target="_blank">Qin Li</a>,
            <a href="https://www.damtp.cam.ac.uk/user/mjc249/home.html" target="_blank">Matthew Colbrook</a>
          </div> -->
        </div>
      </div>
    </div>
  </div>

  <!-- 1-2 -->
  <div class="accordion-item">
    <button class="accordion-trigger" aria-expanded="false">
      Exact Finite-Dimensional Koopman Representations for Polynomial ODEs
      <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </button>
    <div class="accordion-content">
      <div class="topic-inner">
        <div class="topic-text">
          <p>While EDMD yields approximate representations, a more fundamental question is: when does a nonlinear dynamical system admit an <em>exact</em> finite-dimensional Koopman invariant subspace? I am characterizing purely algebraic sufficient and necessary conditions for polynomial ODEs.</p>
          <!-- <div class="collaborators">
            <strong>Collaborators:</strong>
            <a href="https://seewoo5.github.io" target="_blank">Seewoo Lee</a>
          </div> -->
        </div>
      </div>
    </div>
  </div>

  <!-- 1-3 -->
  <div class="accordion-item">
    <button class="accordion-trigger" aria-expanded="false">
      Neural-Network Approach for Non-Autonomous Dynamics
      <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </button>
    <div class="accordion-content">
      <div class="topic-inner">
        <div class="topic-text">
          <p>Classical Koopman theory targets autonomous systems, but many real-world systems are non-autonomous due to time-varying inputs or environmental changes. I am developing a neural-network-based framework to learn Koopman representations for such systems from data, extending the reach of operator-theoretic methods to a broader class of dynamical systems.</p>
          <!-- <div class="collaborators">
            <strong>Collaborators:</strong>
            <a href="https://sites.google.com/view/dae-wook-kim/home" target="_blank">Dae Wook Kim</a>
          </div> -->
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════
     TOPIC GROUP 2 — Mathematical Biology & CRNT
════════════════════════════════════════════════ -->
<div class="topic-group">
  <div class="topic-group-header">
    <!-- <span class="topic-icon">🧬</span> -->
    II. Mathematical Biology: Chemical Reaction Network Theory (CRNT)
  </div>

  <!-- 2-1 -->
  <div class="accordion-item">
    <button class="accordion-trigger" aria-expanded="false">
      Stochastic CRNT: Stationary Distributions of CTMCs
      <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </button>
    <div class="accordion-content">
      <div class="topic-inner">
        <!-- image placeholder: <img src="{{ '/images/research/crn_stationary.png' | relative_url }}" class="topic-image" alt="CRN stationary distribution"> -->
        <div class="topic-text">
          <p>Stochastic biochemical systems are naturally modeled as continuous-time Markov chains (CTMCs). I work on deriving <em>explicit, closed-form</em> stationary distributions for such systems via a technique called <em>network translation</em>, which transforms a given reaction network into one with a more tractable structure. These analytic formulas unlock sensitivity analysis, robustness quantification, and Bayesian likelihood functions that would otherwise be computationally intractable.</p>
          <!-- <div class="collaborators">
            <strong>Collaborators:</strong>
            <a href="https://mathjinsukim.com" target="_blank">Jinsu Kim</a>
          </div> -->
        </div>
      </div>
    </div>
  </div>

  <!-- 2-2 -->
  <div class="accordion-item">
    <button class="accordion-trigger" aria-expanded="false">
      Deterministic CRNT: Steady States and Asymptotic Behavior of ODEs
      <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </button>
    <div class="accordion-content">
      <div class="topic-inner">
        <div class="topic-text">
          <p>In the deterministic setting, biochemical networks are described by ODEs, and a central goal is to understand steady-state behavior — particularly <em>absolute concentration robustness</em> (ACR) and <em>robust perfect adaptation</em> (RPA), whereby certain species concentrations remain invariant to perturbations. I develop structural and algebraic criteria that guarantee such behaviors directly from the network topology, without requiring explicit solutions.</p>
          <!-- <div class="collaborators">
            <strong>Collaborators:</strong>
            <a href="https://people.math.wisc.edu/~craciun/" target="_blank">Gheorghe Craciun</a>,
            <a href="https://sites.google.com/wisc.edu/diego-rojas-la-luz/" target="_blank">Diego Rojas La Luz</a>,
            <a href="https://sites.google.com/site/yujihironooo/" target="_blank">Yuji Hirono</a>,
            <a href="https://wolfram-liebermeister.pages-forge.inrae.fr/web/" target="_blank">Wolfram Liebermeister</a>
          </div> -->
        </div>
      </div>
    </div>
  </div>

  <!-- 2-3 -->
  <div class="accordion-item">
    <button class="accordion-trigger" aria-expanded="false">
      Other Topics: Quasi-Steady-State Approximations &amp; Model Reduction
      <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </button>
    <div class="accordion-content">
      <div class="topic-inner">
        <div class="topic-text">
          <p>Biochemical models often involve species operating on vastly different timescales. Quasi-steady-state approximation (QSSA) exploits this separation to reduce model complexity. I have worked on the validity and universality of such reductions in stochastic settings, establishing conditions under which simplified propensities yield accurate approximations of the full system.</p>
          <!-- <div class="collaborators">
            <strong>Collaborators:</strong>
            <a href="https://mathsci.kaist.ac.kr/~jaekkim/" target="_blank">Jae Kyoung Kim</a>
          </div> -->
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════
     TOPIC GROUP 3 — Inference in Non-Markovian Systems
════════════════════════════════════════════════ -->
<div class="topic-group">
  <div class="topic-group-header">
    <!-- <span class="topic-icon">📊</span> -->
    III. Inference of Parameters in Non-Markovian Systems
  </div>

  <!-- 3-1 -->
  <div class="accordion-item">
    <button class="accordion-trigger" aria-expanded="false">
      Bayesian MCMC for Gene Regulatory Networks and Cell Signaling
      <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </button>
    <div class="accordion-content">
      <div class="topic-inner">
        <!-- image placeholder: <img src="{{ '/images/research/mcmc_delay.png' | relative_url }}" class="topic-image" alt="MCMC inference illustration"> -->
        <div class="topic-text">
          <p>Many biological processes involve unobserved intermediate steps that introduce effective time delays, rendering the system non-Markovian. Drawing on tools from queueing theory, I developed Bayesian MCMC methods to jointly infer kinetic and delay parameters from single-cell data. These methods have been applied to gene regulatory networks and cell signaling pathways, enabling accurate parameter estimation under realistic experimental constraints.</p>
          <!-- <div class="collaborators">
            <strong>Collaborators:</strong>
            <a href="https://mathsci.kaist.ac.kr/~jaekkim/" target="_blank">Jae Kyoung Kim</a>,
            Boseung Choi,
            Krešimir Josić,
            <a href="https://sites.google.com/view/dae-wook-kim/home" target="_blank">Dae Wook Kim</a>
          </div> -->
        </div>
      </div>
    </div>
  </div>

  <!-- 3-2 -->
  <div class="accordion-item">
    <button class="accordion-trigger" aria-expanded="false">
      Infectious Disease Modeling with History-Dependent Dynamics
      <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </button>
    <div class="accordion-content">
      <div class="topic-inner">
        <div class="topic-text">
          <p>Standard compartmental epidemic models assume Markovian transitions, which can introduce systematic bias in parameter estimates. We have developed history-dependent epidemic models, accounting for realistic waiting-time distributions. By applying this method to 2020 Seoul COVID-19 data, we showed that this provides more accurate estimates of key epidemiological parameters</p>
          <!-- <div class="collaborators">
            <strong>Collaborators:</strong>
            <a href="https://mathsci.kaist.ac.kr/~jaekkim/" target="_blank">Jae Kyoung Kim</a>,
            Boseung Choi
          </div> -->
        </div>
      </div>
    </div>
  </div>

  <!-- 3-3 -->
  <div class="accordion-item">
    <button class="accordion-trigger" aria-expanded="false">
      Physics-Informed Machine Learning for Cell Heterogeneity
      <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </button>
    <div class="accordion-content">
      <div class="topic-inner">
        <div class="topic-text">
          <p>Cell-to-cell heterogeneity in signaling responses is a ubiquotous phenomena of biological systems, yet its sources are often difficult to disentangle. In collaboration with <a href="https://sites.google.com/view/hyeontae-site/" target="_blank">Hyeontae Jo</a>, we developed density physics-informed neural networks (Density-PINNs) that directly learn the distribution of parameters from population-level data, identifying key sources of cell-to-cell heterogeneity in antibiotic responses.</p>
          <!-- <div class="collaborators">
            <strong>Collaborators:</strong>
            <a href="https://sites.google.com/view/hyeontae-site/" target="_blank">Hyeontae Jo</a>,
            <a href="https://mathsci.kaist.ac.kr/~jaekkim/" target="_blank">Jae Kyoung Kim</a>
          </div> -->
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════
     TOPIC GROUP 4 — Problem-Driven Collaborative Research
════════════════════════════════════════════════ -->
<div class="topic-group">
  <div class="topic-group-header">
    <!-- <span class="topic-icon">🤝</span> -->
    IV. Problem-Driven Collaborative Research
  </div>
  <div class="topic-standalone">
    <blockquote>"If the only tool you have is a hammer, everything starts to look like a nail."</blockquote>
    <p> In order to address meaningful scientific questions raised by field experts, I believe that the right mathematical framework should be chosen to fit the problem, not the other way around. Beyond developing mathematical theory, I actively engage in collaborations with biologists and clinicians. These projects are motivated by concrete scientific questions, such as identifying digital biomarkers of cognitive impairment from wearable device data, or modeling COVID-19 endemic transition, and often require adapting or extending existing methods in unexpected ways. </p>
  </div>
</div>

<!-- ════════════════════════════════════════════════
     TOPIC GROUP 5 — Other Topics
════════════════════════════════════════════════ -->
<div class="topic-group">
  <div class="topic-group-header">
    <!-- <span class="topic-icon">✦</span> -->
    V. Other Topics
  </div>

  <!-- 5-1 -->
  <div class="accordion-item">
    <button class="accordion-trigger" aria-expanded="false">
      Formalization of Mathematics (LEAN)
      <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </button>
    <div class="accordion-content">
      <div class="topic-inner">
        <div class="topic-text">
          <p>I am contributing to a project on (auto)formalizing graduate-level algebra in the <em>LEAN</em> proof assistant, specifically targeting problems from the textbook <em>Abstract Algebra</em> by Dummit and Foote. We are building a dataset of formalized graduate-level algebra problems, namely <a href="https://www.kaggle.com/datasets/b8d166d6fecce97ae60db6e8a9560e6c015c7db50f609000f72d7cd05b70729d" target="_blank"><strong>LEAN-GAP</strong></a>.
            <!-- This has resulted in <strong>LEAN-GAP</strong>, a dataset of formalized graduate algebra problems. -->
          </p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ── Accordion JS ────────────────────────────── -->
<script>
document.querySelectorAll('.accordion-trigger').forEach(btn => {
  btn.addEventListener('click', () => {
    const content = btn.nextElementSibling;
    const isOpen  = btn.getAttribute('aria-expanded') === 'true';

    // Close all in the same group
    btn.closest('.topic-group').querySelectorAll('.accordion-trigger').forEach(b => {
      b.setAttribute('aria-expanded', 'false');
      b.nextElementSibling.classList.remove('open');
    });

    // Toggle clicked one
    if (!isOpen) {
      btn.setAttribute('aria-expanded', 'true');
      content.classList.add('open');
    }
  });
});
</script>