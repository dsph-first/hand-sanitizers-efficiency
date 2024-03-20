from dash import dash, html, Input, Output, callback, Patch, clientside_callback, dcc
import dash_bootstrap_components as dbc

import app.components.nav_bars.navigation_bar as navig_bar
from app.components.containers.container import controls


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
                        dbc.Row(
                            [
                                html.H4(
                                    ("Sample Distribution"), className="text-center"
                                ),
                                dbc.Col(
                                    dbc.Card(
                                        dcc.Graph(
                                            id="bar_graph",
                                            figure={},
                                        )
                                    ),
                                    lg=6,
                                ),
                                dbc.Col(
                                    dbc.Card(
                                        dcc.Graph(
                                            id="graph",
                                            figure={},
                                        )
                                    ),
                                    lg=6,
                                ),
                            ]
                        ),
                        dbc.Row(
                            [
                                html.H4(
                                    ("Statistical Analysis"), className="text-center"
                                ),
                                dbc.Row(
                                    [
                                        dbc.Row(
                                            [
                                                dcc.RadioItems(
                                                    id="radio-selector",
                                                    options=[
                                                        {
                                                            "label": [
                                                                html.Span(
                                                                    "Two-sample t-test"
                                                                )
                                                            ],
                                                            "value": "Two-sample t-test",
                                                        },
                                                        {
                                                            "label": "Mann-Whitney U",
                                                            "value": "Mann-Whitney U",
                                                        },
                                                    ],
                                                    value="",
                                                    inline=True,
                                                )
                                            ]
                                        ),
                                        dbc.Row(
                                            [
                                                html.Br(),
                                                html.Div(
                                                    id="content-container"),
                                                html.Br(),
                                            ]
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ],
                    # fluid=True,
                ),
            ]
        ),
    ],
    fluid=True,
    className="dbc dbc-ag-grid",
)
