from dash import dash, html, Input, Output, callback, Patch, clientside_callback, dcc
import dash_bootstrap_components as dbc

import app.components.nav_bars.navigation_bar as navig_bar
from app.components.containers.container import controls

# Tabs 
from app.components.tabs.basic_tabs import tabs

basic_layout = dbc.Container(
    [
        navig_bar.navbar,
        dbc.Row(
            [
                dbc.Col(
                    [
                        controls,
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        tabs       
                    ], width = 8,
                    # fluid=True,
                ),
            ]
        ),
    ],
    fluid=True,
    className="dbc dbc-ag-grid",
)
