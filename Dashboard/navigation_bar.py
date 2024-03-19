""" This module is for the navigation bar we have for the dashboard"""

import dash_bootstrap_components as dbc
from dash import dash, html, Input, Output, callback, Patch, clientside_callback,State
import app 
img_source = 'assets/D9PM16520-HD_1.jpg'
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(html.Img(src=img_source, height='30px')),
                    dbc.Col(dbc.NavbarBrand('HandSanitizer', className='mr-auto')),
                ],
                align='center',
                className='g-0',
            ),
            dbc.NavbarToggler(id ="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                id = "navbar-collapse",
                is_open =False,
                navbar = True,      
            ),
        ],
        fluid=True
    ),
    color="dark",
    dark=True,
)
@app.callback(
    Output("navbar-collapse","is_open"),
    [Input('navbar-toggler', 'n_clicks')],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n,is_open):
    if n:
        return not is_open
    return is_open
