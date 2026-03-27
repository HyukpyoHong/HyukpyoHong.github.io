---
layout: default
title: Research
---

<div class="page-header">
  <h1>Research</h1>
</div>

<div class="section">
  <div class="social-links" style="margin-bottom:1.5rem;">
    <a href="https://scholar.google.com/citations?user=SC1r-GAAAAAJ&hl=ko&oi=ao" target="_blank" class="social-link">
      <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" style="width:14px;height:14px;fill:currentColor"><path d="M12 24a7 7 0 1 1 0-14 7 7 0 0 1 0 14zm0-24L0 9.5h3.6v8.4C4.8 19.5 7.9 21 12 21s7.2-1.5 8.4-3.1V9.5H24L12 0z"/></svg>
      Google Scholar
    </a>
    <a href="https://github.com/HyukpyoHong" target="_blank" class="social-link">
      <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" style="width:14px;height:14px;fill:currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
      GitHub
    </a>
  </div>

  <div class="bio-text" style="margin-bottom:1.5rem;">
    <p>My research focuses on central problems in stochastic and deterministic models for complex biological systems. I address questions such as:</p>
    <ul class="question-list">
      <li>How do we efficiently analyze a nonlinear dynamical model despite the huge number of parameters, variables, and equations?</li>
      <li>How do biochemical systems show homeostasis despite fluctuating environmental conditions?</li>
      <li>How do we find a closed form of solutions for dynamical systems?</li>
      <li>How can we accurately estimate unknown parameters in a model with realistic assumptions using Bayesian approaches?</li>
    </ul>
    <p>Recently, after joining UW–Madison as a postdoc, I have been expanding my interest to a more general dynamical system that is not necessarily biological. Specifically, I am working on <strong>Koopman theory</strong>, which offers a (possibly infinite-dimensional) linear representation of a nonlinear dynamical system. The techniques I have developed span the fields of probability, queueing theory, Bayesian inference, and dynamical systems.</p>
  </div>
</div>

<div class="section">
  <div class="section-title">Research Areas</div>

  <div class="research-item">
    <h3>Koopman Theory</h3>
    <p>Koopman theory is a mathematical framework for representing nonlinear dynamical systems using an infinite-dimensional linear operator. This operator acts on a space of measurement functions of the system's state, allowing for a globally linear representation of nonlinear dynamics. I am working on efficient algorithms to find finite-dimensional linear representations that approximate an original nonlinear dynamical system, as well as purely algebraic conditions that allow a given nonlinear dynamical system to admit an <em>exact</em> finite-dimensional representation.</p>
  </div>

  <div class="research-item">
    <h3>Chemical Reaction Network Theory</h3>
    <p>Chemical reaction network theory (CRNT) is a discipline of applied mathematics in which we model a biological/biochemical system using a directed graph representation and infer dynamical properties based on its structural properties. I work on analytic derivation of stationary distributions for the continuous-time Markov chain (CTMC) associated with a stochastic CRN — the steady-state solution of the chemical master equation — which provides long-term information such as sensitivity, robustness, and a likelihood function for Bayesian inference.</p>
  </div>

  <div class="research-item">
    <h3>Bayesian Inference for Non-Markovian Dynamical Systems</h3>
    <p>Not all reactions in a biochemical system can be experimentally measured simultaneously. Replacing unobserved reactions with a single random time delay significantly reduces the number of variables and parameters, but the resulting non-Markovian process makes parameter inference difficult. Based on knowledge from stochastic processes (e.g., queueing theory), I have developed Bayesian MCMC methods to infer system parameters in such non-Markovian systems.</p>
  </div>

  <div class="research-item">
    <h3>Collaborative Works</h3>
    <p><strong>(1) Cognitive Impairment &amp; Wearable Devices.</strong> We use fractal analysis based on detrended fluctuation analysis to find features of activity patterns — measured by wearable devices — that are altered by cognitive impairment, with the goal of enabling pre-diagnosis.</p>
    <p style="margin-top:0.6rem;"><strong>(2) COVID-19 Modeling.</strong> We modeled COVID-19 extinction and endemicity based on two immunities with different longevities: long-lived severity-preventing immunity (T-cell) and short-lived infection-preventing immunity (antibody). Our analysis shows that high viral transmission unexpectedly reduces severe COVID-19 rates during endemic transition, and paradoxically accelerates endemic transition with reduced severe cases in highly vaccinated populations.</p>
  </div>
</div>
