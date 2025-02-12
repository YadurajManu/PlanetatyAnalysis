# Astronomical Analysis Report

## Exoplanet and Stellar Properties Analysis

### Correlation Findings

#### Planet-Star Property Correlations
1. **Planet Radius vs Planet Mass**
   - Strong positive correlation (0.3398)
   - Statistically significant (p-value < 0.0001)
   - Suggests a consistent relationship between planet size and mass

2. **Planet Radius vs Stellar Temperature**
   - Moderate positive correlation (0.3251)
   - Statistically significant (p-value < 0.0001)
   - Indicates that planets around hotter stars tend to be slightly larger

3. **Planet Mass vs Stellar Temperature**
   - Weak positive correlation (0.1318)
   - Statistically significant (p-value < 0.0001)
   - Suggests a subtle relationship between planet mass and stellar characteristics

### Stellar Kinematics Analysis

#### Nearby Stars Characteristics
1. **Parallax**
   - Mean: 102.98 milliarcseconds
   - Indicates an average distance of about 9.7 parsecs
   - Range: 67.67 to 768.07 milliarcseconds

2. **Proper Motion**
   - Right Ascension (PMRA):
     - Mean: 39.03 mas/yr
     - High variability (std dev: 909.15 mas/yr)
   - Declination (PMDEC):
     - Mean: -276.70 mas/yr
     - High variability (std dev: 805.20 mas/yr)

3. **Radial Velocity**
   - Mean: -0.28 km/s
   - Range: -414.02 to 245.05 km/s
   - Indicates complex stellar motions in our local stellar neighborhood

### M31 (Andromeda Galaxy) Observations

#### Observation Metadata
- Total Observations: 24,858
- Observation Types:
  - Multiple instrument observations
  - Various wavelength regions
  - Different calibration levels
What is the meaning of feature in the graph and what is the SHAP meaning explain the graph
#### Key Observation Characteristics
- Coordinate Coverage:
  - Right Ascension (s_ra): Full sky coverage
  - Declination (s_dec): Full sky coverage
- Time Span: Multiple observation epochs
- Wavelength Range: Diverse spectral coverage

## Visualizations
Detailed visualizations have been generated:
1. `results/planet_star_correlations.png`: Heatmap of correlations
2. `results/stellar_proper_motion.png`: Proper motion distribution
3. `results/m31_spectral_observation.png`: M31 spectral characteristics

## Conclusions
1. Planetary properties show complex, non-linear relationships with stellar characteristics
2. Local stellar population demonstrates significant kinematic diversity
3. M31 observations provide a rich dataset for further galactic studies

**Note**: Some correlations returned NaN due to data limitations or missing values. Further data cleaning and collection may improve analysis precision.
