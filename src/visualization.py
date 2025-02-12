import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from pathlib import Path

class AtmosphereVisualizer:
    def __init__(self):
        self.fig = None
    
    def create_interactive_spectrum(self, wavelengths, flux, components=None):
        """Create an interactive spectrum visualization."""
        self.fig = go.Figure()
        
        # Add main spectrum
        self.fig.add_trace(go.Scatter(
            x=wavelengths,
            y=flux,
            mode='lines',
            name='Observed Spectrum',
            line=dict(color='blue', width=2)
        ))
        
        # Add component markers if provided
        if components:
            for component, wavelengths in components.items():
                self.fig.add_trace(go.Scatter(
                    x=wavelengths,
                    y=[np.interp(w, wavelengths, flux) for w in wavelengths],
                    mode='markers',
                    name=f'{component} lines',
                    marker=dict(size=10)
                ))
        
        # Update layout
        self.fig.update_layout(
            title='Interactive Planetary Atmosphere Spectrum',
            xaxis_title='Wavelength (μm)',
            yaxis_title='Normalized Flux',
            hovermode='x',
            template='plotly_white'
        )
        
        return self.fig
    
    def create_composition_chart(self, composition_data):
        """Create a pie chart of atmospheric composition."""
        labels = list(composition_data.keys())
        values = list(composition_data.values())
        
        fig = px.pie(
            values=values,
            names=labels,
            title='Atmospheric Composition'
        )
        
        return fig
    
    def create_biosignature_heatmap(self, biosignature_data):
        """Create a heatmap of biosignature confidence levels."""
        # Convert confidence levels to a matrix format
        confidence_matrix = np.array(list(biosignature_data.values())).reshape(-1, 1)
        
        fig = go.Figure(data=go.Heatmap(
            z=confidence_matrix,
            y=list(biosignature_data.keys()),
            colorscale='Viridis',
            showscale=True
        ))
        
        fig.update_layout(
            title='Biosignature Confidence Levels',
            yaxis_title='Biosignature Type',
            xaxis_visible=False
        )
        
        return fig
    
    def save_visualizations(self, output_dir='results'):
        """Save all visualizations to files."""
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        if self.fig:
            self.fig.write_html(Path(output_dir) / 'interactive_spectrum.html')
            self.fig.write_image(Path(output_dir) / 'spectrum.png')
            
    def display_3d_atmosphere(self, altitude, latitude, longitude, concentration):
        """Create a 3D visualization of atmospheric distribution."""
        fig = go.Figure(data=[go.Volume(
            x=longitude,
            y=latitude,
            z=altitude,
            value=concentration,
            isomin=0.1,
            isomax=0.8,
            opacity=0.1,
            surface_count=25,
        )])
        
        fig.update_layout(
            title='3D Atmospheric Distribution',
            scene=dict(
                xaxis_title='Longitude',
                yaxis_title='Latitude',
                zaxis_title='Altitude'
            )
        )
        
        return fig
