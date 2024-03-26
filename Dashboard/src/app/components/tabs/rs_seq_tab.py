from dash import dash, dcc, html, Input, Output, callback, Patch, clientside_callback, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go


rs_seq_tab = dbc.Tab(
    [
        dbc.Row(
            [
                html.H4(
                    ("Sample Distribution For 16RS Sequencing Test"),
                    className="text-center",
                ),
                # dcc.Dropdown(
                #     id="hand_sanitizer",
                #     options=[
                #         {"label": hand_sanitizers, "value": hand_sanitizers}
                #         for hand_sanitizers in SANITIZERS
                #     ],
                #     # value=ConfigInstance.sanitizers[0]
                # ),
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
    label="16rs Sequencing",
    id="sequencing",
)
