import dash
from dash import dcc, html  # Updated import
import plotly.express as px
import pandas as pd

# Load data
data = pd.read_excel("C:/Users/Chandru/OneDrive/Desktop/Python Visuals/Sample - Superstore.xls", sheet_name="Orders")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Scatter Plot Analysis"),
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': i, 'value': i} for i in data['Category'].unique()],
        value='Furniture',  # Default value
        multi=True
    ),
    dcc.Graph(id='scatter-plot')
])

# Define callback to update graph
@app.callback(
    dash.dependencies.Output('scatter-plot', 'figure'),
    [dash.dependencies.Input('category-dropdown', 'value')]
)
def update_graph(selected_categories):
    # Ensure selected_categories is always a list
    if not isinstance(selected_categories, list):
        selected_categories = [selected_categories]
    
    filtered_data = data[data['Category'].isin(selected_categories)]
    fig = px.scatter(filtered_data, x='Sales', y='Profit', color='Category')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8053)  # Port changed to 8053
