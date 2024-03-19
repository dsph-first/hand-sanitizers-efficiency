"""This is the index file. This file contains the whole skeleton for the dashboards"""
from dash import dash, html, Input, Output, callback, Patch, clientside_callback, dcc
import dash_bootstrap_components as dbc
import navigation_bar
from app import app
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import data_process as dp
import statistics_analysis as st
import counting_colony as cc 
import disk_diffuision as dd
import rs_seq as seq
import user_perceptions as up


hand_sanitizers_list = ["Sagrotan"]

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

#This holds all the tabs. all the tabs layout is in different files.
# cc = colony count, dd = disk diffusion, seq = sequencing, uu = user perceptions
tabs = dbc.Card(dbc.Tabs([cc.tab1, dd.tab2, seq.tab3,up.tab4]))


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
                dbc.Col([tabs], width=8),
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

    # this is demo for the scatter graph
    df = pd.DataFrame(
        {
            "count": [86.111111, 90.833333, 77.277778, 76.055556],
            "sample_type": ["Treated", "Control", "Treated", "Control"],
            "factors": ["HS1", "HS2", "HS2", "HS1"],
        }
    )

    # this dataframe comes from the finger pad test data we had done
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

    # this is generated from demo dataframe
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
                                "which is less than 0.05. So there is significant difference between the efficasy  of the hand sanitizer and the control (Washing with water and soap).",
                                className="card-text",
                            ),
                        ]
                    ),
                ]
            ),
        )


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=True)