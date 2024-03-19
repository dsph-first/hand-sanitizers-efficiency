
"""This module is full working module before adding the tabs"""

from dash import dash, html, Input, Output, callback, Patch, clientside_callback, dcc
import dash_bootstrap_components as dbc
import navigation_bar
from app import app
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import data_process as dp
import statistics_analysis as st


hand_sanitizers_list = ["Sagrotan"]
# hs_dropdown = dcc.Dropdown(
#     [
#     dbc.Label('Select the non-alcoholic hand-sanitizer'),

#      className = 'dropdown',
#     ],
# )

hs_dropdown = html.Div(
    [
        dbc.Label("Select the non-alcoholic hand-sanitizer"),
        dcc.Dropdown(
            id="hand_sanitizer",
            options=[
                {"label": hand_sanitizers, "value": hand_sanitizers}
                for hand_sanitizers in hand_sanitizers_list
            ],
        ),
    ]
)

initial_paragraph_content = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4(
                            html.B(
                                "Elevate Your Hygiene: Exploring the Effectiveness of Non-Alcoholic Hand Sanitizers through our Dashboard"
                            ),
                            className="text-primary",
                        ),
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            """Hand hygine is very essential to prevent the infections. Non-alcoholic hand sanitizer significantly
                    reduce the presence of microbes presents on hands after using the product compared to a neutral control.
                    
                    """
                        )
                    ]
                )
            ]
        ),
    ],
    fluid=True,
)
controls = dbc.Card(
    [initial_paragraph_content, hs_dropdown],
    body=True,
)


app.layout = dbc.Container(
    [
        navigation_bar.navbar,
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
                                                html.Div(id="content-container"),
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


@callback(
    [
        Output(component_id="bar_graph", component_property="figure"),
        Output(component_id="graph", component_property="figure"),
    ],
    [Input(component_id="hand_sanitizer", component_property="value")],
)
def update(hand_sanitizer):

    df = pd.DataFrame(
        {
            "count": [86.111111, 90.833333, 77.277778, 76.055556],
            "sample_type": ["Treated", "Control", "Treated", "Control"],
            "factors": ["HS1", "HS2", "HS2", "HS1"],
        }
    )

    # data_frame = pd.DataFrame({

    # })

    global df_result
    df_result = dp.return_dataframe(hand_sanitizer)
    # print(df_result)
    fig = px.bar(
        df_result,
        x="HS",
        y="count",
        color="Sample_type",
        barmode="group",
        labels={"HS": "Hand Sanitizer", "count": "Count"},
        color_discrete_sequence=["#225ea8", "#41b6c4"],
        error_y="SEM_mean",
        error_y_minus="SEM_mean",
    )

    fig.update_layout(
        title="Number of colonies per Hand Sanitizer",
        xaxis_title="Hand Sanitizers",
        yaxis_title="Number of colonies",
        legend_title="Factors",
    )

    fig_another = px.scatter(
        df,
        x="factors",
        y="count",
        color="sample_type",
        labels={"count": "Count"},
        color_discrete_sequence=["#225ea8", "#41b6c4"],
    )

    fig_another.update_layout(
        title="Another Chart",
        xaxis_title="Hand Sanitizers",
        yaxis_title="Count",
        legend_title="Sample Type",
    )

    return fig, fig_another


@app.callback(
    Output("content-container", "children"), [Input("radio-selector", "value")]
)
def update_content(selected_option):
    print(selected_option, df_result)
    stat_value, p_value = st.stat_analysis(selected_option, df_result)

    print(stat_value, p_value)

    if p_value > 0.05:
        p_value = "{0:.4f}".format(p_value)
        stat_value = "{0:.4f}".format(stat_value)
        print(">0.05")
        return html.Div(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4(selected_option, className="card-title"),
                            html.Br(),
                            html.H6(
                                "Statistical value: "
                                + str(stat_value)
                                + ", P value: "
                                + str(p_value),
                                className="card-subtitle",
                            ),
                            html.Br(),
                            # html.H6("Statistical value:", stat_value, 'P value', p_value, className="card-subtitle"),
                            html.P(
                                # 'Statistical value:', str(stat_value),'P value:',str(p_value),"\n",
                                " Here p value is "
                                + str(p_value)
                                + "which is greater than 0.05. So there is no significant difference between the efficay  of the hand sanitizer and the control (Washing with water and soap).",
                                className="card-text",
                            ),
                        ]
                    ),
                ]
            )
        )
    if p_value < 0.05:
        p_value = "{0:.2f}".format(p_value)
        stat_value = str(stat_value)
        print("<0.05")
        return html.Div(
            html.Br(),
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4(selected_option, className="card-title"),
                            html.H6(
                                "Statistical value:",
                                str(stat_value),
                                "P value:",
                                str(p_value),
                                className="card-subtitle",
                            ),
                            html.P(
                                "Statistical value:",
                                str(stat_value),
                                "P value:",
                                str(p_value),
                                "Here p value is",
                                str("{:.3f}".format(p_value)),
                                "which is less than 0.05. So there is significant difference between the efficay  of the hand sanitizer and the control (Washing with water and soap).",
                                className="card-text",
                            ),
                        ]
                    ),
                ]
            ),
        )


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=True)
