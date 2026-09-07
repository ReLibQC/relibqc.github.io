---
layout: default
title: "The Julia language in atomistic modelling: Software integration across research communities"
speaker: "Michael Herbst"
affiliation: "EPFL"
type: "Keynote talk"
---

# The Julia language in atomistic modelling: Software integration across research communities

**Speaker:** Michael Herbst
**Affiliation:** EPFL
**Type:** Keynote talk

---

### Abstract

Recent years have seen growing adoption of the Julia programming language for atomistic modelling, particularly for developing robust and differentiable simulation codes. Julia-based efforts now encompass density-functional theory (DFT) --- exemplified by the Density-Functional ToolKit (DFTK, https://dftk.org) --- the construction of ACE-based interatomic potentials (https://acesuit.github.io/), and molecular dynamics simulations in Molly.jl (https://juliamolsim.github.io/Molly.jl).
                                                                                                 
Focusing on DFTK I provide an overview of Julia's unique ability to lead to concise, efficient and readable DFT code, which supports research endeavours from multiple communities. Right now, with about 10k lines of code, DFTK remains tractable, despite we recently managed to considerably expand its features. Examples are the scaling to multiple GPUs, end-to-end differentiability as well as advanced and expensive electronic structure models, such as Hybrid DFT or DFT with Hubbard corrections. I will argue how focusing primarily on keeping the code base small enabled us to fully exploit advantages of differentiable programming and in this way nevertheless achieve state-of-the-art performance.

Zooming out I will provide an overview of ongoing efforts in the broader JuliaMolSim (https://juliamolsim.org) ecosystem for atomistic modelling in Julia. In particular I want to highlight efforts to extend the accessibility of Julia tools beyond the Julia environment, e.g. to supply compiled Julia modules to simulation engines such as LAMMPS written in foreign languages.    
                                                                                                 
This talk reports on work that has been conducted by many people from the DFTK an JuliaMolSim communities, some of which has been conducted without my personal involvement.

---

[← Return to main schedule]({{ site.baseurl }}/)
