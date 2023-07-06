import pandas as pd
import dash
from dash import dcc
from dash import html

# Read the Excel file
df = pd.read_excel('Online Retail.xlsx')

# Filter data for the year 2011
df_2011 = df[df['InvoiceDate'].dt.year == 2011]

# Group by month and calculate revenue
revenue_by_month = df_2011.groupby(df_2011['InvoiceDate'].dt.month)['UnitPrice'].sum()

# Create Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1('Revenue Time Series for 2011'),
    dcc.Graph(
        id='revenue-time-series',
        figure={
            'data': [
                {'x': revenue_by_month.index, 'y': revenue_by_month, 'type': 'line', 'name': 'Revenue'},
            ],
            'layout': {
                'title': 'Monthly Revenue',
                'xaxis': {'title': 'Month'},
                'yaxis': {'title': 'Revenue'}
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
