# Particle Decay Simulator

This program simulates the decay of a particle into two daughter particles, specifically a muon and an antimuon (denoted as mu+ and mu-, respectively). The simulation is based on the Standard Model of particle physics, using the `scikit-hep` package for handling four-vectors and particle properties.

## Code Structure

The code is composed of a class `ParticleDecaySimulator` which contains all the necessary methods to simulate the decay of a given particle.

### The `ParticleDecaySimulator` class

- **Initialization (`__init__`):** Takes a PDG ID as an argument and creates a `Particle` instance from the PDG ID using the `Particle` class from the `particle` package.

- **`simulate_decay` method:** Simulates the decay process for the particle instance. It divides the rest mass energy of the mother particle into two equal parts and assigns them to the daughter muon and antimuon. This is an oversimplification as in a realistic scenario, the energy distribution would depend on the specific decay process dynamics.

- **`run` method:** Executes the decay simulation multiple times, as specified by the `num_decays` parameter. It prints out the four-momenta of the resulting mu+ and mu- particles for each decay event.

- **`print_decay_products` static method:** A utility method for printing the four-momenta of the decay products in a readable format.

### Constants and Assumptions

- The speed of light `c` is imported from `scipy.constants` to ensure the correct conversion of mass to energy using Einstein's equation \( E = mc^2 \).

- The mass of the particle is taken directly from the `Particle` instance without considering any kinetic energy or potential energy that might be present in an actual decay event.

### Random Momenta Generation

- Directional cosines and phi angles for the momenta are randomly generated to simulate a uniform distribution of decay directions in 3D space.

### Energy and Momentum Conservation

- To conserve energy and momentum, the program assigns equal and opposite momenta to the mu+ and mu- particles, ensuring that the total momentum of the system remains zero, as expected for a particle decaying at rest.

### The LorentzVector

- `LorentzVector` objects from the `skhep.math.vectors` package are used to represent the four-momenta of the particles. These objects conveniently handle spacetime calculations in high-energy physics.

## Program Output

The output of the program lists the four-momenta of mu+ and mu- pairs for ten decay events of a J/Psi particle. Here's an example of one line of output:

Four-momentum of mu+ (px, py, pz, E): (2.446059029175029e+18, -9.75106019680138e+19, 9.926409586946667e+19, 1.3916774565150253e+20)
Four-momentum of mu- (px, py, pz, E): (-2.446059029175029e+18, 9.75106019680138e+19, -9.926409586946667e+19, 1.3916774565150253e+20)



Each line shows the momentum components (px, py, pz) and energy (E) for a mu+ and mu- particle. The energies are the same for both daughter particles, which aligns with the assumption of equal energy distribution. The momentum components have the same magnitude but opposite signs, indicating momentum conservation.

## Usage

To use this program:

1. Make sure you have `scikit-hep`, `particle`, and `hepunits` installed in your Python environment.
2. Save the `ParticleDecaySimulator` class code to a file.
3. Run the file to simulate the decay of a J/Psi particle into muon pairs.

## Conclusion

This simulation is a simplified model meant for educational purposes and to demonstrate the use of four-vectors and particle properties in a Pythonic simulation environment.
