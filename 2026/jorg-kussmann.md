---
layout: default
title: "A Modular Approach for Program-Independent Ab Initio Method Development"
speaker: "Jörg Kussmann"
affiliation: "Theoretical Chemistry, Ludwig-Maximilians-Universität München (LMU)"
type: "Contributed talk"
---

# A Modular Approach for Program-Independent Ab Initio Method Development

**Speaker:** Jörg Kussmann
**Affiliation:** Theoretical Chemistry, Ludwig-Maximilians-Universität München (LMU)
**Type:** Contributed talk

---

### Abstract

A Modular Approach for Program-Independent Ab Initio Method Development


Jörg Kussmann, Theoretical Chemistry, Ludwig-Maximilians-Universität München (LMU)


I propose a modular strategy for ab initio electronic program packages,
which enables them to be used directly as a development platform for external
developers. Therefore, new developments do not have to be either tied to or be
adapted by a specific program package, but instead can be used directly with
any software offering the proposed interface.

In order to enable easy access to the functionality of the backend library, a
frontend class is proposed [1] which allows convenient access to low- and
high-level functions and classes of the backend library.

The modular design is demonstrated at the example of the FermiONs++ program
package [2], which provides interfaces not only for C++, but also for other
programming languages like Python, Rust, Julia, and Zig.

After a general description on the design of a general access class for
electronic structure codes, first examples using the FermiONs++ interface will
be presented using also different programming languages.

Finally, a first practical tool developed with the C++ interface is presented
which allows for massively parallelized non-orthogonal configuration
interaction calculations (NOCI-COOX [3]).

[1] https://codeberg.org/CommonQC/QCBackend
[2] J. Kussmann and C. Ochsenfeld, J. Chem. Phys. 138, 134114 (2013);
    J. Kussmann and C. Ochsenfeld, J. Chem. Theory Comput. 11, 918 (2015).
[3] Y. Lemke, J. Kussmann, and C. Ochsenfeld, J. Chem. Theory Comput. 21, 10193 (2025).

---

[← Return to main schedule]({{ site.baseurl }}/)
