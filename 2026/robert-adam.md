---
layout: default
title: "SeQuant Goes Multireference: What This Can Teach Us About Reusable Library Design"
speaker: "Robert Adam"
affiliation: "University of Stuttgart"
type: "Short talk"
---

# SeQuant Goes Multireference: What This Can Teach Us About Reusable Library Design

**Speaker:** Robert Adam
**Affiliation:** University of Stuttgart
**Type:** Short talk

---

### Abstract

Community adoption is the defining metric of success for reusable libraries, yet it remains the most formidable challenge for developers. This is particularly true if adopters
work outside the maintainer's immediate area of research. We encountered this difficulty first-hand while integrating SeQuant, an open-source automation framework for method
development in many-body physics and quantum chemistry, into our development workflow for methods based on internally-contracted multireference coupled cluster (icMRCC) theory.
Previously, SeQuant had been used for single-reference methods only. Unsurprisingly, several technical challenges emerged when applying it to icMRCC methods. Particularly, in functions related to symbolic spin-integration and subsequent transformation into a biorthogonal basis as well as the ones related to expression canonicalization. To get everything
working we had to get involved in SeQuant development and contribute several changes aimed at generalizing those routines. With this, we made SeQuant compatible with icMRCC
theory and lowered the barrier for further community adoption.
In this talk, we will recapitulate our most significant contributions to SeQuant. We will illustrate our experience from the adopters' point of view and evaluate what has and what could have been done during initial SeQuant development to pave the way for such extensions. Overall, we will distill a set of guidelines for the development of reusable libraries that we
believe promote extensibility, the foundation of a thriving collaborative community.

---

[← Return to main schedule]({{ site.baseurl }}/)
