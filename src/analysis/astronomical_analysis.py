import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

class AstronomicalAnalyzer:
    def __init__(self, data_dir='data/raw'):
        """
        Initialize the analyzer with data from various astronomical sources
        """
        self.data_dir = data_dir
        self.load_datasets()

    def load_datasets(self):
        """
        Load datasets from different astronomical sources
        """
        # NASA Exoplanet data
        self.exoplanets = pd.read_csv(f'{self.data_dir}/nasa_exoplanets.csv')
        
        # SIMBAD Planetary data
        self.simbad_planets = pd.read_csv(f'{self.data_dir}/simbad_planet.csv')
        
        # Gaia Stellar data
        self.gaia_stars = pd.read_csv(f'{self.data_dir}/gaia_nearby_stars.csv')
        
        # MAST M31 data
        self.mast_m31 = pd.read_csv(f'{self.data_dir}/mast_m31.csv')

    def clean_exoplanet_data(self):
        """
        Clean and preprocess exoplanet data
        """
        # Remove rows with missing critical values
        self.exoplanets.dropna(subset=['pl_radj', 'pl_bmassj', 'st_teff'], inplace=True)
        
        # Convert units if necessary
        # Jupiter radii to Earth radii
        self.exoplanets['pl_rade'] = self.exoplanets['pl_radj'] * 10.97  
        
        # Jupiter masses to Earth masses
        self.exoplanets['pl_masse'] = self.exoplanets['pl_bmassj'] * 317.8  

    def analyze_planet_star_correlations(self):
        """
        Analyze correlations between planetary and stellar properties
        """
        # Prepare correlation analysis
        correlation_data = self.exoplanets[['pl_rade', 'pl_masse', 'pl_orbper', 'st_teff', 'st_rad']]
        
        # Compute correlation matrix
        corr_matrix = correlation_data.corr()
        
        # Visualize correlation matrix
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlation between Planetary and Stellar Properties')
        plt.tight_layout()
        plt.savefig('results/planet_star_correlations.png')
        plt.close()

        # Statistical tests
        print("Correlation Analysis Results:")
        for col1 in correlation_data.columns:
            for col2 in correlation_data.columns:
                if col1 != col2:
                    correlation, p_value = stats.pearsonr(correlation_data[col1], correlation_data[col2])
                    print(f"Correlation between {col1} and {col2}: {correlation:.4f} (p-value: {p_value:.4f})")

    def analyze_stellar_kinematics(self):
        """
        Analyze nearby stars' kinematics from Gaia data
        """
        # Basic statistical summary
        print("\nNearby Stars Kinematics Summary:")
        print(self.gaia_stars[['parallax', 'pmra', 'pmdec', 'radial_velocity']].describe())
        
        # Visualize proper motion distribution
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        sns.histplot(self.gaia_stars['pmra'], kde=True)
        plt.title('Proper Motion (RA)')
        plt.xlabel('Proper Motion (mas/yr)')
        
        plt.subplot(1, 2, 2)
        sns.histplot(self.gaia_stars['pmdec'], kde=True)
        plt.title('Proper Motion (Dec)')
        plt.xlabel('Proper Motion (mas/yr)')
        
        plt.tight_layout()
        plt.savefig('results/stellar_proper_motion.png')
        plt.close()

    def analyze_m31_observations(self):
        """
        Analyze MAST observations of M31 (Andromeda Galaxy)
        """
        # Basic information about M31 observations
        print("\nM31 Observations Summary:")
        print(self.mast_m31.info())
        
        # If observation details are available, create some visualizations
        if 'wavelength' in self.mast_m31.columns and 'flux' in self.mast_m31.columns:
            plt.figure(figsize=(10, 6))
            plt.plot(self.mast_m31['wavelength'], self.mast_m31['flux'])
            plt.title('M31 Spectral Observations')
            plt.xlabel('Wavelength')
            plt.ylabel('Flux')
            plt.savefig('results/m31_spectral_observation.png')
            plt.close()

    def generate_report(self):
        """
        Generate a comprehensive astronomical analysis report
        """
        # Ensure results directory exists
        import os
        os.makedirs('results', exist_ok=True)
        
        # Clean data
        self.clean_exoplanet_data()
        
        # Perform analyses
        self.analyze_planet_star_correlations()
        self.analyze_stellar_kinematics()
        self.analyze_m31_observations()

def main():
    analyzer = AstronomicalAnalyzer()
    analyzer.generate_report()

if __name__ == "__main__":
    main()
