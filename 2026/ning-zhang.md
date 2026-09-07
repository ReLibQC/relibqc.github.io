---
layout: default
title: "MetaWave: A Platform for Unified Implementation of Wave Function Methods"
speaker: "Ning Zhang"
affiliation: "Qingdao Institute for Theoretical and Computational Sciences and Center for Optics Research and Engineering, Shandong University"
type: "Short talk"
---

# MetaWave: A Platform for Unified Implementation of Wave Function Methods

**Speaker:** Ning Zhang
**Affiliation:** Qingdao Institute for Theoretical and Computational Sciences and Center for Optics Research and Engineering, Shandong University
**Type:** Short talk

---

### Abstract

The development of reusable libraries is increasingly recognized as a key strategy to reduce software maintenance costs and accelerate scientific progress in quantum chemistry. However, implementing wave function methods that work seamlessly across diverse Hamiltonians and wave function ansätze often leads to massive code duplication and high maintenance overhead.Moreover,integrating quantum chemical methods with high-performance computing is essential for treating large systems at moderate accuracy or small systems at high accuracy, which further adds to the complexity.
In this talk, we present MetaWave, a C++ template-based platform designed to address these challenges by decoupling three distinct aspects of quantum chemical methods: the nature of the Hamiltonian, the structure of the wave function, and the parallelization strategy. This decoupling enables a unified implementation of wave function methods. Second-quantized Hamiltonians, including nonrelativistic (spin-free), relativistic (spin-dependent), and other types such as those arising in cavity quantum electrodynamics, are first decomposed into topologically equivalent diagrams. This allows a unified evaluation of the basic coupling coefficients between spin-free or spin-dependent configuration state functions (CSFs) or Slater determinants that incorporate full molecular symmetry. As a result, wave functions built from either scalar or spinor orbitals can be assembled using the same templates. Unified parallelization is achieved by first abstracting every computational step of a method as a dynamically scheduled loop, followed by a global reduction of local results from each computational unit (thread or process). This algorithmic abstraction enables the use of a single algorithm template applied to each step of the given wave function method to achieve parallelization. Using iCIPT2 as a showcase, we demonstrate how it can be extended from the nonrelativistic Hamiltonian to various Hamiltonians and efficiently parallelized via MetaWave, as well as its application to strongly correlated systems.

---

[← Return to main schedule]({{ site.baseurl }}/)
