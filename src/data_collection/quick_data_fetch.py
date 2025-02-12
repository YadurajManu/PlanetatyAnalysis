import pandas as pd
import numpy as np

class QuickAstronomicalDataset:
    def __init__(self):
        # Pre-defined sample sizes to keep it fast
        self.exoplanet_sample_size = 500
        self.star_sample_size = 300

    def generate_synthetic_exoplanet_data(self):
        """
        Generate a quick synthetic exoplanet dataset
        """
        np.random.seed(42)  # For reproducibility
        
        data = {
            'planet_name': [f'Exo-{i}' for i in range(self.exoplanet_sample_size)],
            'star_name': [f'Star-{np.random.randint(1, 1000)}' for _ in range(self.exoplanet_sample_size)],
            'planet_radius': np.random.uniform(0.5, 20, self.exoplanet_sample_size),  # Jupiter radii
            'planet_mass': np.random.uniform(0.1, 10, self.exoplanet_sample_size),   # Jupiter masses
            'orbital_period': np.random.uniform(1, 500, self.exoplanet_sample_size),  # Days
            'star_temperature': np.random.uniform(3000, 10000, self.exoplanet_sample_size),  # Kelvin
            'habitable_zone': np.random.choice([True, False], self.exoplanet_sample_size)
        }
        
        df = pd.DataFrame(data)
        df.to_csv('data/raw/quick_exoplanets.csv', index=False)
        print("✅ Quick Exoplanet Dataset Generated")
        return df

    def generate_synthetic_star_data(self):
        """
        Generate a quick synthetic stellar dataset
        """
        np.random.seed(42)  # For reproducibility
        
        data = {
            'star_name': [f'Star-{i}' for i in range(self.star_sample_size)],
            'right_ascension': np.random.uniform(0, 360, self.star_sample_size),
            'declination': np.random.uniform(-90, 90, self.star_sample_size),
            'distance': np.random.uniform(10, 1000, self.star_sample_size),  # Light years
            'temperature': np.random.uniform(3000, 50000, self.star_sample_size),
            'luminosity': np.random.uniform(0.1, 100000, self.star_sample_size),
            'spectral_type': np.random.choice(['O', 'B', 'A', 'F', 'G', 'K', 'M'], self.star_sample_size)
        }
        
        df = pd.DataFrame(data)
        df.to_csv('data/raw/quick_stars.csv', index=False)
        print("✅ Quick Stellar Dataset Generated")
        return df

    def generate_quick_datasets(self):
        """
        Generate both exoplanet and stellar datasets quickly
        """
        exoplanets = self.generate_synthetic_exoplanet_data()
        stars = self.generate_synthetic_star_data()
        
        print("\n📊 Dataset Summary:")
        print(f"Exoplanets: {len(exoplanets)} records")
        print(f"Stars: {len(stars)} records")

def main():
    quick_data = QuickAstronomicalDataset()
    quick_data.generate_quick_datasets()

if __name__ == "__main__":
    main()
