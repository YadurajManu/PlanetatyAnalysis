import os
import shutil
import json
from datetime import datetime

class ProjectFinalizer:
    def __init__(self, project_root='/Users/sujeetkumarsingh/Desktop/planetary_analysis'):
        self.project_root = project_root
        self.timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    def create_project_summary(self):
        """
        Generate a comprehensive project summary
        """
        summary = {
            "project_name": "Astronomical Machine Learning Analysis",
            "finalization_timestamp": self.timestamp,
            "key_achievements": [
                "Developed synthetic astronomical datasets",
                "Created machine learning models for exoplanet prediction",
                "Implemented advanced model interpretation techniques",
                "Explored data collection strategies"
            ],
            "model_performance": {
                "habitable_zone_classifier": {
                    "accuracy": "54-55%",
                    "key_features": [
                        "Planet radius",
                        "Planet mass", 
                        "Orbital period",
                        "Star temperature"
                    ]
                },
                "planet_radius_regressor": {
                    "mean_squared_error": "0.0026-0.0031"
                }
            },
            "future_recommendations": [
                "Collect more diverse astronomical datasets",
                "Refine feature engineering techniques",
                "Explore advanced machine learning algorithms",
                "Seek additional astronomical data sources"
            ]
        }

        # Create a final project summary
        summary_path = os.path.join(self.project_root, f'project_summary_{self.timestamp}.json')
        with open(summary_path, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print("📄 Project Summary Created:")
        print(json.dumps(summary, indent=2))
        return summary

    def cleanup_intermediate_files(self):
        """
        Remove unnecessary and intermediate files
        """
        # Directories to clean
        cleanup_dirs = [
            'results/ml_models',
            'results/model_interpretation',
            'data/raw/nasa_exoplanets'
        ]

        # Files to remove
        cleanup_files = [
            'src/data_collection/advanced_data_aggregator.py',
            'src/data_collection/comprehensive_data_strategy.py',
            'src/ml_models/exoplanet_predictor.py',
            'src/ml_models/exoplanet_model_interpreter.py'
        ]

        # Remove directories
        for dir_path in cleanup_dirs:
            full_path = os.path.join(self.project_root, dir_path)
            if os.path.exists(full_path):
                try:
                    shutil.rmtree(full_path)
                    print(f"🗑️ Removed directory: {full_path}")
                except Exception as e:
                    print(f"❌ Could not remove {full_path}: {e}")

        # Remove files
        for file_path in cleanup_files:
            full_path = os.path.join(self.project_root, file_path)
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f"🗑️ Removed file: {full_path}")
                except Exception as e:
                    print(f"❌ Could not remove {full_path}: {e}")

    def create_readme(self):
        """
        Create a final README for the project
        """
        readme_content = """# Astronomical Machine Learning Analysis

## Project Overview
This project explores machine learning techniques for exoplanet and astronomical data analysis.

### Key Components
- Synthetic data generation
- Exoplanet prediction models
- Advanced model interpretation

### Quick Start
1. Explore the `src/ml_models/advanced_exoplanet_predictor.py` for the main model
2. Check `results/astronomical_analysis_report.md` for detailed analysis

### Future Work
- Expand dataset collection
- Improve model accuracy
- Explore advanced machine learning techniques

### Contact
For more information, please reach out to the project maintainer.
"""
        
        readme_path = os.path.join(self.project_root, 'README.md')
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        
        print("📘 README.md created successfully")

def main():
    print("🚀 Planetary Analysis Project Finalizer 🌌")
    
    finalizer = ProjectFinalizer()
    
    # Create project summary
    finalizer.create_project_summary()
    
    # Cleanup intermediate files
    finalizer.cleanup_intermediate_files()
    
    # Create README
    finalizer.create_readme()
    
    print("\n✨ Project finalization complete!")

if __name__ == "__main__":
    main()
