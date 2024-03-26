""" This module is for the navigation bar we have for the dashboard"""

from dash import html, Input, Output, callback, State
import dash_bootstrap_components as dbc
from index import HandSanitizerAppInstance
import os

# TODO
# need to get the assest url for showing any pictures in the dash
# this also add circular error
url = HandSanitizerAppInstance.dash_app.get_asset_url()
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(html.Img(src=url, height='30px')),
                    dbc.Col(dbc.NavbarBrand(
                        'HandSanitizer', className='mr-auto')),
                ],
                align='center',
                className='g-0',
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ],
        fluid=True
    ),
    color="dark",
    dark=True,
)


@callback(
    Output("navbar-collapse", "is_open"),
    [Input('navbar-toggler', 'n_clicks')],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open