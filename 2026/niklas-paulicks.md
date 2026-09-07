---
layout: default
title: "Benchmarking Least-Squares Tensor Hypercontraction Techniques for Molecular Systems"
speaker: "Niklas Paulicks"
affiliation: "University of Hamburg"
type: "Flash talk"
---

# Benchmarking Least-Squares Tensor Hypercontraction Techniques for Molecular Systems

**Speaker:** Niklas Paulicks
**Affiliation:** University of Hamburg
**Type:** Flash talk

---

### Abstract

Exploiting sparsity in the two-electron integral (ERI) tensor is a crucial step toward reducing the computational cost of many-body electronic structure methods. In recent years, a range of tensor factorization techniques, such as the tensor hypercontraction (THC) approach [1], have been developed to achieve this goal. In particular, linear optimization techniques based on least-squares (LS) fitting are of special interest because of their algorithmic simplicity, which may enable their application to large-scale systems.

Unfortunately, the landscape of these THC techniques remains highly fragmented, and many closely related methods have been developed independently in the literature, including LS-THC [1], interpolative separable density fitting (ISDF) [2], and RI-RS [3]. In this talk, I will present a unifying perspective on these approaches, which has enabled their efficient implementation in a newly developed library, PyTHC [4].

This new library enables, for the first time, a systematic comparison of the various linear THC techniques on an equal footing. To this end, I will present an in-depth assessment of these methods for a subset of the GMTKN55 benchmark database [5].

[1] R. M. Parrish, E. G. Hohenstein, T. J. Martínez, and C. D. Sherrill, J. Chem. Phys. 137, 224106 (2012)
[2] J. Lu, L. Ying, J. Comput. Phys. 302, 329 (2015)
[3] I. Duchemin, X. Blase, J. Chem. Phys. 150, 174120 (2019)
[4] N. Paulicks, J. Tölle, in preparation
[5] L. Goerigk, A. Hansen, C. Bauer, S. Ehrlich, A. Najibi, S. Grimme, Phys. Chem. Chem. Phys. 19, 32184 (2017)

---

[← Return to main schedule]({{ site.baseurl }}/)
