import dash
#import dash_core_components as dcc
#import dash_html_components as html
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

# Create a Dash Application
app=dash.Dash(__name__)
server=app.server

# Define the layout of the Dashboard
app.layout = html.Div(
    [
         dbc.Row([
            dbc.Col(
                [
                    html.H1('My Dashboard')
                ],  
                width=12
            ),
        ]) ,   
        dbc.Row([
            dbc.Col(
                [
                    html.Img(src='assets/Bridges.jpg', width="1000", height="600")
                ],  
                width=12
            ),
        ])    
    ]
)



# Run the application
if __name__ == "__main__":
    app.run(debug=True)
