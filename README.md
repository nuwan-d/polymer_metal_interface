# Molecular Dynamics Simulation of a Polymer-Metal Interface

We are currently investigating [the ballistic impact resistance of polymer-metal multilayers using molecular dynamics.](https://www.linkedin.com/pulse/mechanical-behaviour-nanomaterials-under-shock-nuwan-dewapriya/) This project showed us that modelling material interfaces could be challenging even for someone with a background in atomic simulations. Therefore, we thought of sharing some useful information and the LAMMPS input files required to model the aluminum-polyurethane system shown below. A movie of the simulation is [vaialable here](https://youtu.be/Nx7B1W6U_m8).

 <img src="image.PNG" width="300">

# Modelling of polyurethane:
Modelling a polymer can be challenging depending on the complexity of an individual polymer chain. The structure of the polyurethane chain shown in the above video can be depicted as below.
Polymer chain schematic 
I created the polymer chain using the [Enhanced Monte Carlo Package](http://montecarlo.sourceforge.net/emc/Welcome.html) by Pieter J. in ’t Veld. Another useful package to build polymers is [Moltemplate](https://www.moltemplate.org/) by Andrew Jewett. 

Mark Tschopp has provided an overview of [modelling a polymer chain](https://github.com/mrkllntschpp/lammps-tutorials/blob/master/LAMMPS-Tutorials-08.ipynb) and a [amorphous polyethylene sample](https://icme.hpc.msstate.edu/mediawiki/index.php/Deformation_of_Amorphous_Polyethylene) in LAMMPS. Moreover, Appendix A of the reference [1] and the reference [2] also provide some useful information about modelling polymers. I used the polymer consistent force field (PCFF) for modelling polyurea.

# Modelling of aluminum:
create_atoms command in LAMMPS can be used to model aluminum. [In this tutorial](https://github.com/mrkllntschpp/lammps-tutorials/blob/master/LAMMPS-Tutorials-03.ipynb) Mark Tschopp outlines how to use create_atoms command to generate a grain boundary. 
I used the [EAM potential by Adams and Ercolessi](https://openkim.org/id/EAM_Dynamo_ErcolessiAdams_1994_Al__MO_123629422045_005) to model aluminum. 

# Combining aluminum and polyurethane:
The two data files (i.e. polyurethane and aluminum) can be combined using MATLAB or even MS Excel. When combining the two models, careful attention needed to be paid to the image flags of the atoms in the polymer chain to make sure that they do not have crossed the periodic boundary.
In this simulation, the non-bonded interactions between aluminum and polyurea were modelled using the van der Waals parameters obtained from the [interface force field](https://bionanostructures.com/interface-md/). 

Many questions related to LAMMPS have been answered on the [LAMMPS mail list](https://lammps.sandia.gov/mail.html). If you want to learn the basics of atomistic simulations of fracture, the book [Modeling Materials: Continuum, Atomistic and Multiscale Techniques](http://www.modelingmaterials.org/the-books) could be useful.

I hope that this information will be useful for those who are interested in modelling material interfaces.

# References
[1] A.P. Awasthi, D.C. Lagoudas, D.C. Hammerand, Modeling of graphene–polymer interfacial mechanical behavior using molecular dynamics, Model. Simul. Mater. Sci. Eng. 17 (2009) 015002.

[2] D. Hossain, M.A. Tschopp, D.K. Ward, J.L. Bouvard, P. Wang, M.F. Horstemeyer, Molecular dynamics simulations of deformation mechanisms of amorphous polyethylene, Polymer 51 (2010) pp. 6071-6083.
