import requests
import pandas as pd
import numpy as np
from pathlib import Path
from astroquery.nasa_exoplanet_archive import NasaExoplanetArchive
from astroquery.mast import Observations
from astroquery.simbad import Simbad
from astroquery.gaia import Gaia
import logging
from datetime import datetime, timedelta
import json

class ComprehensiveSpaceDataCollector:
    def __init__(self, output_dir='data/raw'):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('comprehensive_data_collection.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def fetch_comprehensive_exoplanets(self):
        """
        Fetch comprehensive exoplanet data with multiple filters
        """
        try:
            self.logger.info("Fetching comprehensive exoplanet data...")
            
            # More extensive list of columns
            columns = [
                'pl_name', 'hostname', 'pl_orbper', 'pl_radj', 'pl_bmassj',
                'pl_orbeccen', 'pl_eqt', 'st_teff', 'st_rad', 'st_mass',
                'pl_discmethod', 'pl_locale', 'pl_telescope', 
                'pl_instrument', 'pl_status', 'pl_mnum'
            ]
            
            # Multiple query strategies
            queries = [
                # Confirmed planets
                ("confirmed", "default_flag=1"),
                # Potentially habitable
                ("habitable", "pl_eqt BETWEEN 200 AND 400"),
                # Large planets
                ("large_planets", "pl_radj > 1"),
                # Planets in multi-planet systems
                ("multi_planet", "pl_mnum > 1")
            ]
            
            for query_name, where_clause in queries:
                try:
                    data = NasaExoplanetArchive.query_criteria(
                        table="ps",
                        select=columns,
                        where=where_clause
                    )
                    
                    output_file = self.output_dir / f'nasa_exoplanets_{query_name}.csv'
                    data.write(output_file, format='csv', overwrite=True)
                    self.logger.info(f"Saved {query_name} exoplanet data to {output_file}")
                except Exception as sub_error:
                    self.logger.warning(f"Failed to fetch {query_name} exoplanet data: {sub_error}")
            
            return True
        except Exception as e:
            self.logger.error(f"Comprehensive exoplanet data collection error: {str(e)}")
            return False

    def fetch_extended_stellar_data(self):
        """
        Fetch extended stellar data from multiple sources
        """
        try:
            self.logger.info("Fetching extended stellar data...")
            
            # Gaia advanced query
            gaia_query = """
            SELECT TOP 5000
                source_id, ra, dec, parallax, pmra, pmdec,
                phot_g_mean_mag, bp_rp, radial_velocity,
                teff_val, radius_val, mass_val,
                ruwe, non_single_star
            FROM gaiadr3.gaia_source
            WHERE parallax > 5  # Within ~200 parsecs
            AND phot_g_mean_mag < 15  # Bright stars
            AND bp_rp IS NOT NULL
            ORDER BY parallax DESC
            """
            
            job = Gaia.launch_job(gaia_query)
            gaia_results = job.get_results()
            
            output_file = self.output_dir / 'gaia_extended_stars.csv'
            gaia_results.write(output_file, format='csv', overwrite=True)
            self.logger.info(f"Saved extended Gaia stellar data to {output_file}")
            
            return True
        except Exception as e:
            self.logger.error(f"Extended stellar data collection error: {str(e)}")
            return False

    def fetch_spectral_library(self):
        """
        Fetch spectral data from multiple astronomical sources
        """
        try:
            self.logger.info("Fetching spectral library data...")
            
            # MAST multi-mission spectral query
            spectral_targets = ['star', 'galaxy', 'nebula', 'exoplanet']
            
            for target in spectral_targets:
                obs_table = Observations.query_criteria(
                    dataproduct_type='spectrum',
                    target_classification=target
                )
                
                if len(obs_table) > 0:
                    output_file = self.output_dir / f'mast_spectral_{target}.csv'
                    obs_table.write(output_file, format='csv', overwrite=True)
                    self.logger.info(f"Saved {target} spectral data to {output_file}")
            
            return True
        except Exception as e:
            self.logger.error(f"Spectral library data collection error: {str(e)}")
            return False

    def generate_synthetic_planetary_systems(self, num_systems=1000):
        """
        Generate synthetic planetary system data for machine learning
        """
        try:
            self.logger.info(f"Generating {num_systems} synthetic planetary systems...")
            
            # Synthetic data generation with realistic constraints
            synthetic_systems = []
            
            for _ in range(num_systems):
                # Star properties
                star_temp = np.random.uniform(3000, 10000)  # Kelvin
                star_mass = np.random.uniform(0.1, 3)  # Solar masses
                star_radius = np.random.uniform(0.1, 3)  # Solar radii
                
                # Planet system properties
                num_planets = np.random.randint(1, 7)
                planets = []
                
                for _ in range(num_planets):
                    planet = {
                        'radius': np.random.lognormal(0, 0.5),  # Jupiter radii
                        'mass': np.random.lognormal(0, 0.5),  # Jupiter masses
                        'orbital_period': np.random.lognormal(1, 1),  # Days
                        'temperature': np.random.uniform(50, 1000)  # Kelvin
                    }
                    planets.append(planet)
                
                system = {
                    'star_temperature': star_temp,
                    'star_mass': star_mass,
                    'star_radius': star_radius,
                    'planets': planets
                }
                
                synthetic_systems.append(system)
            
            output_file = self.output_dir / 'synthetic_planetary_systems.json'
            with open(output_file, 'w') as f:
                json.dump(synthetic_systems, f, indent=2)
            
            self.logger.info(f"Saved synthetic planetary systems to {output_file}")
            return True
        except Exception as e:
            self.logger.error(f"Synthetic planetary system generation error: {str(e)}")
            return False

def main():
    collector = ComprehensiveSpaceDataCollector()
    
    # Comprehensive data collection
    collector.fetch_comprehensive_exoplanets()
    collector.fetch_extended_stellar_data()
    collector.fetch_spectral_library()
    collector.generate_synthetic_planetary_systems()

if __name__ == "__main__":
    main()
