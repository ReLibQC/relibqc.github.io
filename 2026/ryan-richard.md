---
layout: default
title: "Efforts to Create Modular Floating-Point Independent Software"
speaker: "Ryan Richard"
affiliation: "Ames National Laboratory"
type: "Contributed talk"
---

# Efforts to Create Modular Floating-Point Independent Software

**Speaker:** Ryan Richard
**Affiliation:** Ames National Laboratory
**Type:** Contributed talk

---

### Abstract

Most electronic structure packages explicitly assume double precision floating point types. Alternative numeric representations (e.g., single precision, quadruple precision, automatically-differentiable) are becoming increasingly important for scientific applications. The diversification is being driven not only by hardware/performance, but also by application (e.g., not wanting to derive analytic derivatives by hand). While C++'s template mechanism offers a potential solution, it can be tricky to exploit this mechanism at language boundaries which can in turn inhibit the creation of reusable software that relies on languages other than C++. The point of this talk is to bring this problem to the community's attention and to discuss NWChemEx's efforts to provide a reusable solution.

---

[← Return to main schedule]({{ site.baseurl }}/)
