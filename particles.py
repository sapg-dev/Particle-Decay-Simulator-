from skhep.math.vectors import LorentzVector
from particle import Particle
from hepunits import units as u
import numpy as np
from scipy.constants import c
class ParticleDecaySimulator:
    def __init__(self, pdg_id):
        self.particle = Particle.from_pdgid(pdg_id)

    def simulate_decay(self):
        # Here, 'self.particle' is the mother particle that will decay
        mu_plus = Particle.from_pdgid(13)  # mu+
        mu_minus = Particle.from_pdgid(-13) # mu-

        # Calculate mass and create decay products
        mass = self.particle.mass  # Mother particle's mass

        # Assume the rest mass energy is equally distributed (over-simplified)
        energy_per_daughter = mass / 2 * c**2  # Convert to energy using E=mc^2

        # Randomly generate momentum direction
        costheta = 2 * np.random.rand() - 1
        sintheta = np.sqrt(1 - costheta**2)
        phi = 2 * np.pi * np.random.rand()
        px = sintheta * np.cos(phi) * energy_per_daughter
        py = sintheta * np.sin(phi) * energy_per_daughter
        pz = costheta * energy_per_daughter

        # Create the four-vectors for each daughter particle
        p4_mu_plus = LorentzVector(px, py, pz, energy_per_daughter)
        p4_mu_minus = LorentzVector(-px, -py, -pz, energy_per_daughter)

        # Return the four-momentum vectors of the decay products
        return p4_mu_plus, p4_mu_minus

    def run(self, num_decays):
        for _ in range(num_decays):
            p4_mu_plus, p4_mu_minus = self.simulate_decay()
            self.print_decay_products(p4_mu_plus, p4_mu_minus)

    @staticmethod
    def print_decay_products(p4_mu_plus, p4_mu_minus):
        print("Four-momentum of mu+ (px, py, pz, E):", p4_mu_plus)
        print("Four-momentum of mu- (px, py, pz, E):", p4_mu_minus)

# Example usage
if __name__ == "__main__":
    simulator = ParticleDecaySimulator(443)  # J/Psi particle
    simulator.run(10)  # Simulate the decay 10 times
