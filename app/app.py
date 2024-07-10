import dash
from dash import html
from dash.dependencies import Input, Output, State
import dash_leaflet as dl
import json
from geojson import Feature, FeatureCollection, Polygon

app = dash.Dash(__name__)

# estilos para el poligono dibujado
draw_options = {
    'polygon': {'shapeOptions': {'color': '#00ff00'}},
    'polyline': False,
    'rectangle': False,
    'circle': False,
    'circlemarker': False,
    'marker': False
}

# armo el layout de la app 
app.layout = html.Div([
    html.H1("Mapa interactivo para dibujar y guardar polígonos"),
    dl.Map([
        dl.TileLayer(),
        dl.FeatureGroup([
            dl.EditControl(
                id="edit_control",
                position="topright",
                draw=draw_options,
            )
        ])
    ], style={'width': '100%', 'height': '85vh'}, center=[0, 0], zoom=2),
    html.Button('Guardar GeoJSON', id='save-button', n_clicks=0),
    html.Div(id='output-message')
])

@app.callback(
    Output('output-message', 'children'),
    Input('save-button', 'n_clicks'),
    State('edit_control', 'geojson'),
    prevent_initial_call=True
)

def save_geojson(n_clicks, geojson_data):
    if n_clicks > 0 and geojson_data:
        features = []
        for feature in geojson_data['features']:
            if feature['geometry']['type'] == 'Polygon':
                polygon = Polygon(feature['geometry']['coordinates'])
                features.append(Feature(geometry=polygon))
        
        feature_collection = FeatureCollection(features)
        
        with open('assets/polygon.geojson', 'w') as f:
            json.dump(feature_collection, f)
        
        return "GeoJSON guardado como 'polygons.geojson'"
    return "No hay datos para guardar"

if __name__ == '__main__':
    app.run_server(debug=True)