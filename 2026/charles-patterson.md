---
layout: default
title: "Density-fitting method in the Exciton code for GW and BSE methods"
speaker: "Charles Patterson"
affiliation: "Trinity College Dublin, Ireland"
type: "Flash talk"
---

# Density-fitting method in the Exciton code for GW and BSE methods

**Speaker:** Charles Patterson
**Affiliation:** Trinity College Dublin, Ireland
**Type:** Flash talk

---

### Abstract

Density-fitting method in the Exciton code for GW and BSE methods  

Charles H. Patterson, School of Physics, Trinity College Dublin, Ireland 

Exciton is a gaussian orbital code for excitations in molecules and solids which has been applied to electronic excitations in clusters [1], molecules [2,3] and solids [4,5] and positron binding [6] and scattering and annihilation in molecules using GW, the Bethe-Salpeter equation (BSE) and related methods. The GW and BSE methods for solids using coulomb-metric density-fitting have recently been implemented in Exciton and applied to wide and narrow gap semiconductors.  For GW calculations on both molecules and solids, the screened coulomb interaction, W, is obtained using W = v + vΠv rather than the inverse dielectric matrix screened coulomb potential which is commonly used in plane-wave GW codes. The former approach does not require a plasmon pole approximation. The polarizability, Π, in W is treated at the RPA level. RPA polarizabilities require solution of Bethe-Salpeter equations (BSE) at unique q points.  Wave function and auxiliary fitting basis sets are all electron gaussian basis sets adapted from the def2-TZVP basis sets of Weigend and Ahlrichs. Addition of high angular momentum wave function basis functions up to ℓ = 4 allows the free electron band structure for MgO to be reproduced to around 100 eV. Beginning from a HF band structure, the GoWo@HF self-energy corrects most of the band gap and band width errors in the HF band structure. The method has been applied to diamond, Si, MgO, and anatase and rutile TiO2 [5]. Solution of the BSE for both zero momentum transfer (optical excitations) and finite momentum transfer (electron energy loss) is possible. Assembly of an RPA or BSE Hamiltonian matrix using density-fitting two and three-centre coulomb integrals is fast (around 10 s per unique q-point for 4 valence bands and 32 conduction bands on an 8x8x8 mesh). Diagonalisation of the resulting 32000 x 32000 matrix takes 85 s using ELPA on 8 Nvidia H200 GPUs. The way is open to application of these methods to systems with large unit cells.

[1] doi.org/10.1103/PhysRevMaterials.3.043804 
[2] doi.org/10.1021/acs.jctc.4c00795 
[3] doi.org/10.1063/5.0236385  
[4] doi.org/10.1063/5.0014106  
[5] arxiv.org/abs/2605.19746  
[6] doi.org/10.1038/s41586-022-04703-3

---

[← Return to main schedule]({{ site.baseurl }}/)
