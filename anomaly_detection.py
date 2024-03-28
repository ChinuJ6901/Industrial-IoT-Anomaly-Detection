# Import necessary libraries
import dash
from dash import dcc, html
import pandas as pd

# Load data
data = pd.read_csv('anomaly_data.csv')

# Initialize Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div(children=[
    html.H1(children='Industrial IoT Anomaly Detection Dashboard'),
    dcc.Graph(
        id='anomaly-graph',
        figure={
            'data': [
                {'x': data.index, 'y': data[col], 'type': 'line', 'name': col} for col in data.columns[:-1]
            ],
            'layout': {
                'title': 'Sensor Readings',
                'xaxis': {'title': 'Time'},
                'yaxis': {'title': 'Value'}
            }
        }
    ),
    html.Br(),
    html.H3(children='Anomaly Detection Results'),
    dcc.Graph(
        id='anomaly-counts',
        figure={
            'data': [
                {'x': data['Anomaly'].value_counts().index, 'y': data['Anomaly'].value_counts().values, 'type': 'bar'}
            ],
            'layout': {
                'title': 'Anomaly Counts',
                'xaxis': {'title': 'Status'},
                'yaxis': {'title': 'Count'}
            }
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
