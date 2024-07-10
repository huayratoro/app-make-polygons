# Interactive Polygon Drawing Map

This Dash application allows users to interactively draw polygons on a map and export the drawings as GeoJSON files.

## Features

- Interactive map interface
- Polygon drawing tools
- Export drawn polygons as GeoJSON

## Requirements

- Python 3.10+
- Dash
- dash-leaflet
- geojson

## Installation

1. Clone this repository
2. Install the required packages:

    ```bash
    pip install dash dash-leaflet geojson

## Usage

1. Run the application:

    ```python 
    python app.py

2. Open a web browser and navigate to `http://127.0.0.1:8050/`

3. Use the drawing tools on the top right of the map to create polygons.

4. Click the "Guardar GeoJSON" button to save the drawn polygons as a GeoJSON file.

## How it works

- The application uses Dash and dash-leaflet to create an interactive map interface.
- Users can draw polygons on the map using the provided drawing tools.
- When the "Guardar GeoJSON" button is clicked, the application processes the drawn polygons and saves them as a GeoJSON file named 'polygon.geojson' in the 'assets' folder.

## Customization

- You can modify the `draw_options` dictionary to enable or disable specific drawing tools.
- The map's initial center and zoom level can be adjusted in the `dl.Map` component.
