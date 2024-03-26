from dash import dash, html, Input, Output, callback, Patch, clientside_callback, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

# need to get the model name from the appInstance
# this gives circular dependency error
get_stat_model ='Mann-Whitney U'

counting_colony_tab = dbc.Tab(
    [
        dbc.Row(
            [
                html.H4(("Sample Distribution For counting colony Test"),
                        className="text-center"),
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
                html.H4(("Statistical Analysis"), className="text-center"),
                dbc.Row(
                    [
                        dbc.Row(
                            [
                                dcc.RadioItems(
                                    id="radio-selector",
                                    options=[
                                        {
                                            "label": [html.Span(get_stat_model)],
                                            "value": get_stat_model,
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
                                html.Div(id="content-container"),
                                html.Br(),
                            ]
                        ),
                    ]
                ),
            ]
        ),
    ],
    label='Counting Colony'
)
