import os
import requests
import pandas as pd

class AstronomicalDatasetDownloader:
    def __init__(self, download_dir='data/raw'):
        self.download_dir = download_dir
        os.makedirs(download_dir, exist_ok=True)

    def download_nasa_exoplanet_data(self):
        """Download NASA Exoplanet Archive Complete Dataset"""
        url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+ps&format=csv"
        file_path = os.path.join(self.download_dir, 'nasa_exoplanet_complete.csv')
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            with open(file_path, 'wb') as f:
                f.write(response.content)
            
            print(f"✅ NASA Exoplanet Dataset downloaded: {file_path}")
            return file_path
        except Exception as e:
            print(f"❌ Download failed: {e}")
            return None

    def download_kaggle_exoplanet_dataset(self):
        """Download Curated Exoplanet Dataset from Kaggle-like sources"""
        datasets = [
            {
                'name': 'exoplanet_confirmed',
                'url': 'https://raw.githubusercontent.com/OpenExoplanetCatalogue/open_exoplanet_catalogue/master/data/systems.csv'
            },
            {
                'name': 'exoplanet_candidates',
                'url': 'https://raw.githubusercontent.com/NASA-Planetary-Science/planetary_data/main/exoplanets.csv'
            }
        ]
        
        downloaded_files = []
        for dataset in datasets:
            try:
                response = requests.get(dataset['url'])
                response.raise_for_status()
                
                file_path = os.path.join(self.download_dir, f'{dataset["name"]}.csv')
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                
                downloaded_files.append(file_path)
                print(f"✅ {dataset['name']} downloaded: {file_path}")
            except Exception as e:
                print(f"❌ {dataset['name']} download failed: {e}")
        
        return downloaded_files

    def download_stellar_datasets(self):
        """Download Stellar Datasets"""
        stellar_datasets = [
            {
                'name': 'gaia_nearby_stars',
                'url': 'https://gea.esac.esa.int/archive/tap/sync?query=select+top+10000+source_id,ra,dec,parallax,pmra,pmdec,phot_g_mean_mag+from+gaiadr3.gaia_source+where+parallax%3E10&format=csv'
            }
        ]
        
        downloaded_files = []
        for dataset in stellar_datasets:
            try:
                response = requests.get(dataset['url'])
                response.raise_for_status()
                
                file_path = os.path.join(self.download_dir, f'{dataset["name"]}.csv')
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                
                downloaded_files.append(file_path)
                print(f"✅ {dataset['name']} downloaded: {file_path}")
            except Exception as e:
                print(f"❌ {dataset['name']} download failed: {e}")
        
        return downloaded_files

    def summarize_datasets(self):
        """Provide summary of downloaded datasets"""
        datasets = [
            f for f in os.listdir(self.download_dir) 
            if f.endswith('.csv')
        ]
        
        print("\n🔍 Dataset Summary:")
        for dataset in datasets:
            file_path = os.path.join(self.download_dir, dataset)
            df = pd.read_csv(file_path)
            print(f"{dataset}:")
            print(f"  - Total Records: {len(df)}")
            print(f"  - Columns: {', '.join(df.columns[:5])}...\n")

def main():
    downloader = AstronomicalDatasetDownloader()
    
    print("🚀 Downloading Astronomical Datasets...")
    downloader.download_nasa_exoplanet_data()
    downloader.download_kaggle_exoplanet_dataset()
    downloader.download_stellar_datasets()
    
    downloader.summarize_datasets()

if __name__ == "__main__":
    main()
