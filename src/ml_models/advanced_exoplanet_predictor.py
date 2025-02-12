import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    classification_report, 
    accuracy_score, 
    mean_squared_error, 
    confusion_matrix
)
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

class AdvancedExoplanetPredictor:
    def __init__(self, data_path='data/raw/quick_exoplanets.csv'):
        # Create results directory
        self.results_dir = 'results/advanced_ml_models'
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Load and preprocess data
        self.data = pd.read_csv(data_path)
        self.prepare_data()

    def prepare_data(self):
        """
        Advanced data preparation with feature engineering
        """
        # Original features
        base_features = [
            'planet_radius', 
            'planet_mass', 
            'orbital_period', 
            'star_temperature'
        ]
        
        # Feature engineering
        self.data['radius_mass_ratio'] = self.data['planet_radius'] / (self.data['planet_mass'] + 1e-5)
        self.data['orbital_temp_ratio'] = self.data['orbital_period'] / (self.data['star_temperature'] + 1e-5)
        
        # Expanded feature set
        features = base_features + ['radius_mass_ratio', 'orbital_temp_ratio']
        
        # Separate features and targets
        self.X = self.data[features]
        self.y_habitable = self.data['habitable_zone']
        self.y_radius = self.data['planet_radius']

    def create_advanced_pipeline(self, model_type='classifier'):
        """
        Create advanced machine learning pipeline
        """
        if model_type == 'classifier':
            # Advanced classifier pipeline
            pipeline = Pipeline([
                ('poly', PolynomialFeatures(degree=2, include_bias=False)),
                ('scaler', StandardScaler()),
                ('classifier', GradientBoostingClassifier(
                    n_estimators=200, 
                    learning_rate=0.1, 
                    max_depth=3, 
                    random_state=42
                ))
            ])
            
            # Hyperparameter tuning
            param_grid = {
                'classifier__n_estimators': [100, 200, 300],
                'classifier__learning_rate': [0.01, 0.1, 0.5],
                'classifier__max_depth': [3, 4, 5]
            }
            
            return pipeline, param_grid
        
        else:
            # Advanced regressor pipeline
            pipeline = Pipeline([
                ('poly', PolynomialFeatures(degree=2, include_bias=False)),
                ('scaler', StandardScaler()),
                ('regressor', RandomForestRegressor(
                    n_estimators=200, 
                    max_depth=10, 
                    random_state=42
                ))
            ])
            
            # Hyperparameter tuning
            param_grid = {
                'regressor__n_estimators': [100, 200, 300],
                'regressor__max_depth': [5, 10, 15]
            }
            
            return pipeline, param_grid

    def train_habitable_zone_classifier(self):
        """
        Advanced habitable zone classification
        """
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y_habitable, test_size=0.2, random_state=42
        )
        
        # Create pipeline and grid search
        pipeline, param_grid = self.create_advanced_pipeline('classifier')
        
        # Grid search with cross-validation
        grid_search = GridSearchCV(
            pipeline, 
            param_grid, 
            cv=5, 
            scoring='accuracy', 
            n_jobs=-1
        )
        
        # Fit and predict
        grid_search.fit(X_train, y_train)
        best_model = grid_search.best_estimator_
        
        # Predictions
        y_pred = best_model.predict(X_test)
        
        # Performance metrics
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred)
        
        # Visualize confusion matrix
        plt.figure(figsize=(8, 6))
        sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
        plt.title('Habitable Zone Prediction Confusion Matrix')
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.tight_layout()
        plt.savefig(os.path.join(self.results_dir, 'habitable_zone_confusion_matrix.png'))
        plt.close()
        
        # Save best model and results
        joblib.dump(best_model, os.path.join(self.results_dir, 'best_habitable_zone_classifier.joblib'))
        
        with open(os.path.join(self.results_dir, 'habitable_zone_classification_report.txt'), 'w') as f:
            f.write(f"Best Parameters: {grid_search.best_params_}\n\n")
            f.write(f"Accuracy: {accuracy:.2%}\n\n")
            f.write(report)
        
        print("🌍 Advanced Habitable Zone Classifier:")
        print(f"Best Parameters: {grid_search.best_params_}")
        print(f"Accuracy: {accuracy:.2%}")
        print(f"Classification Report:\n{report}")
        
        return best_model

    def train_planet_radius_regressor(self):
        """
        Advanced planet radius regression
        """
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y_radius, test_size=0.2, random_state=42
        )
        
        # Create pipeline and grid search
        pipeline, param_grid = self.create_advanced_pipeline('regressor')
        
        # Grid search with cross-validation
        grid_search = GridSearchCV(
            pipeline, 
            param_grid, 
            cv=5, 
            scoring='neg_mean_squared_error', 
            n_jobs=-1
        )
        
        # Fit and predict
        grid_search.fit(X_train, y_train)
        best_model = grid_search.best_estimator_
        
        # Predictions
        y_pred = best_model.predict(X_test)
        
        # Performance metrics
        mse = mean_squared_error(y_test, y_pred)
        
        # Visualization of predictions
        plt.figure(figsize=(10, 6))
        plt.scatter(y_test, y_pred, alpha=0.5)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
        plt.title('Advanced Predicted vs Actual Planet Radius')
        plt.xlabel('Actual Radius')
        plt.ylabel('Predicted Radius')
        plt.tight_layout()
        plt.savefig(os.path.join(self.results_dir, 'advanced_radius_prediction_plot.png'))
        plt.close()
        
        # Save best model
        joblib.dump(best_model, os.path.join(self.results_dir, 'best_planet_radius_regressor.joblib'))
        
        with open(os.path.join(self.results_dir, 'planet_radius_regression_report.txt'), 'w') as f:
            f.write(f"Best Parameters: {grid_search.best_params_}\n\n")
            f.write(f"Mean Squared Error: {mse:.4f}\n")
        
        print("\n🪐 Advanced Planet Radius Regressor:")
        print(f"Best Parameters: {grid_search.best_params_}")
        print(f"Mean Squared Error: {mse:.4f}")
        
        return best_model

def main():
    print("🚀 Advanced Exoplanet Machine Learning Model 🌌")
    
    # Initialize and train models
    ml_model = AdvancedExoplanetPredictor()
    
    # Train advanced habitable zone classifier
    ml_model.train_habitable_zone_classifier()
    
    # Train advanced planet radius regressor
    ml_model.train_planet_radius_regressor()

if __name__ == "__main__":
    main()
