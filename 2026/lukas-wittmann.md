---
layout: default
title: "The Modular and Open-Source Implicit Solvation Toolbox MOIST"
speaker: "Lukas Wittmann"
affiliation: "Mulliken Center for Theoretical Chemistry, University of Bonn, Beringstraße 4, D-53115 Bonn, Germany"
type: "Short talk"
---

# The Modular and Open-Source Implicit Solvation Toolbox MOIST

**Speaker:** Lukas Wittmann
**Affiliation:** Mulliken Center for Theoretical Chemistry, University of Bonn, Beringstraße 4, D-53115 Bonn, Germany
**Type:** Short talk

---

### Abstract

Implicit solvation models are often implemented separately in individual quantum-chemistry programs, duplicating effort, making consistency more difficult, and limiting model availability. To address these issues, we present MOIST, a reusable library for implicit solvation and integral-equation models.
MOIST is implemented in Fortran with C and Python interfaces and couples to host codes via a simple API: the host provides only quantities required by the chosen solvation model, and MOIST returns solvation energies and, if needed, properties and derivatives.
The library provides modular base classes for cavities, model components, and complete models; this allows solvation methods to be assembled and extended from reusable building blocks. Besides empirical model components [1], MOIST supports sophisticated terms such as continuum-integrated dispersion, as well as integral-equation formalisms including Reference Interaction Site Model variants [2] and molecular Ornstein-Zernike theory.
In addition, MOIST serves as a standalone driver for models and components that do not require an explicit QM-coupling and provides a development platform for new methods. We highlight two ongoing developments enabled by MOIST: a fully smooth and differentiable solvent-excluded-surface-like cavity discretization scheme [3], and GEMS, a general and minimally empirical solvation model.

[1] Ehlert, S., Stahn, M., Spicher, S., Grimme, S., J. Chem. Theory Comput., 2021, 17 (7), 4250-4261.
[2] Hirofumi, S., Phys. Chem. Chem. Phys., 2013, 15, 20, 7450-7465.
[3] Wittmann, L., Pausch, A., 2026, manuscript in preparation.

---

[← Return to main schedule]({{ site.baseurl }}/)
