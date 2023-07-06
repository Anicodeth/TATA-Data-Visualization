import dash
from dash import dcc
from dash import html
import pandas as pd

# Set the chunk size for pagination
chunk_size = 100000


df = pd.read_excel("Online Retail.xlsx",  skiprows=range(1, 100000),  nrows=chunk_size)

# Create Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1('Invoice Data Analysis'),
    dcc.Graph(
        id='quantity-by-country',
        figure={
            'data': [
                {'x': df['Country'], 'y': df['Quantity'], 'type': 'bar', 'name': 'Quantity'},
            ],
            'layout': {
                'title': 'Quantity by Country'
            }
        }
    ),
    dcc.Graph(
        id='revenue-by-country',
        figure={
            'data': [
                {'x': df['Country'], 'y': df['Quantity']*df['UnitPrice'], 'type': 'bar', 'name': 'Revenue'},
            ],
            'layout': {
                'title': 'Revenue by Country'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)