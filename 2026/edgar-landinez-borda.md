---
layout: default
title: "Exploring Performance Portability in QMCkl: A Kokkos-Based Orbital Microbenchmark"
speaker: "Edgar Landinez Borda"
affiliation: "Juelich Super Computing Center"
type: "Flash talk"
---

# Exploring Performance Portability in QMCkl: A Kokkos-Based Orbital Microbenchmark

**Speaker:** Edgar Landinez Borda
**Affiliation:** Juelich Super Computing Center
**Type:** Flash talk

---

### Abstract

The practical application of Quantum Monte Carlo (QMC) methods relies on highly optimized computational kernels. Supporting these kernels on heterogeneous architectures has traditionally required maintaining separate CPU and GPU implementations, increasing development and maintenance effort. This work investigates the use of Kokkos in the Quantum Monte Carlo kernel library (QMCkl) to provide a single implementation of the atomic and molecular orbital (AO/MO) kernels across multiple hardware backends.

We implemented a hardware-dispatch layer that intercepts the existing C/Fortran API calls and forwards them to a C++ Kokkos implementation. The dispatch mechanism is integrated into the QMCkl context, preserving the existing user API. Performance portability is evaluated on multicore CPUs with OpenMP and NVIDIA Ampere GPUs with CUDA by comparing the Kokkos implementation against the existing platform-specific kernels.

---

[← Return to main schedule]({{ site.baseurl }}/)
