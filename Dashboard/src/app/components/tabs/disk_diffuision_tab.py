from dash import dash, html, Input, Output, callback, Patch, clientside_callback, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go


disk_diffuision_tab = dbc.Tab(
    [
        dbc.Row(
            [
                html.H4(("Sample Distribution For disk Difuision Test"),
                        className="text-center"),
                dbc.Col(
                    #     dbc.Card(
                    #         dcc.Graph(
                    #             id="bar_graph",
                    #             figure={},
                    #         )
                    #     ),
                    #     lg=6,
                    # ),
                    # dbc.Col(
                    #     dbc.Card(
                    #         dcc.Graph(
                    #             id="graph",
                    #             figure={},
                    #         )
                    #     ),
                    #     lg=6,
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
                                # dcc.RadioItems(
                                #     id="radio-selector",
                                #     options=[
                                #         {
                                #             "label": [html.Span("Two-sample t-test")],
                                #             "value": "Two-sample t-test",
                                #         },
                                #         {
                                #             "label": "Mann-Whitney U",
                                #             "value": "Mann-Whitney U",
                                #         },
                                #     ],
                                #     value="",
                                #     inline=True,
                                # )
                            ]
                        ),
                        dbc.Row(
                            [
                                # html.Br(),
                                # html.Div(id="content-container"),
                                # html.Br(),
                            ]
                        ),
                    ]
                ),
            ]
        ),
    ],
    label='Disk Diffusion Test'
)
