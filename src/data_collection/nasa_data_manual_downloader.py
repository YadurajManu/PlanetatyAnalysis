import os
import requests

class NASADataDownloader:
    def __init__(self, output_dir='data/raw/nasa_exoplanets'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        # Curated NASA dataset URLs
        self.datasets = {
            'confirmed_exoplanets': 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+ps+where+pl_disposition+=+%27Confirmed%27&format=csv',
            'planetary_systems': 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+pscomppars&format=csv'
        }

    def download_dataset(self, dataset_name):
        """
        Download a specific NASA dataset
        """
        try:
            url = self.datasets[dataset_name]
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            output_file = os.path.join(self.output_dir, f'{dataset_name}.csv')
            
            with open(output_file, 'wb') as f:
                f.write(response.content)
            
            print(f"✅ Downloaded {dataset_name}")
            print(f"Saved to: {output_file}")
            
            return output_file
        
        except Exception as e:
            print(f"❌ Download failed for {dataset_name}: {e}")
            return None

    def download_all_datasets(self):
        """
        Download all available datasets
        """
        downloaded_files = {}
        
        for dataset_name in self.datasets.keys():
            file_path = self.download_dataset(dataset_name)
            if file_path:
                downloaded_files[dataset_name] = file_path
        
        return downloaded_files

def main():
    print("🚀 NASA Exoplanet Dataset Manual Downloader 🌍")
    
    downloader = NASADataDownloader()
    downloader.download_all_datasets()

if __name__ == "__main__":
    main()
