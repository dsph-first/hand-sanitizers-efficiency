
"""This module is full working module before adding the tabs"""

from dash import dash, html, Input, Output, callback, Patch, clientside_callback, dcc
import plotly.express as px
import pandas as pd
import logging
from scipy.stats import sem

from config.config import Config
from app.app import HandSanitizerApplication
from app.components.layout import Layout
from app.components.divs.p_value import get_p_value_higher_div, get_p_value_less_div

global HandSanitizerAppInstance

# global DF


@callback(
        
    Output("content-container", "children"), [Input("radio-selector", "value")]
)
def update_content(selected_option=None):
    print(' ====================== update_content ======================')
    if selected_option == "" or selected_option == None:
        return html.Div()

    stat_value, p_value = HandSanitizerAppInstance.calculate_stats_for_model(
        selected_option)
    print(stat_value, p_value)

    if stat_value == None or p_value == None:
        return
    if p_value > 0.05:
        p_value = "{0:.4f}".format(p_value)
        stat_value = "{0:.4f}".format(stat_value)
        return get_p_value_higher_div(selected_option, stat_value, p_value)
    if p_value < 0.05:
        p_value = "{0:.2f}".format(p_value)
        stat_value = str(stat_value)
        return get_p_value_less_div(selected_option, stat_value, p_value)


@callback(
    # [
        Output(component_id="bar_graph", component_property="figure"),
        # Output(component_id="graph", component_property="figure"),
    # ],
    [Input(component_id="hand_sanitizer", component_property="value")],
)
def update(hand_sanitizer):
    print(' ====================== UPDATE ======================')
    fig = px.bar()
    if hand_sanitizer != None:
        df_result = HandSanitizerAppInstance.get_df_for(hand_sanitizer)
        # DF= df_result
        # DF = HandSanitizerAppInstance.check_distribution()
        fig = px.bar(
            df_result,
            x="HS",
            y="count",
            color="Sample_type",
            barmode="group",
            labels={"HS": "Hand Sanitizer", "count": "Count"},
            color_discrete_sequence=["#225ea8", "#41b6c4"],
            error_y=[sem(df_result.iloc[0:1, :6].values.tolist(), axis=None, ddof=0), sem(
                df_result.iloc[1, :6].values.tolist(), axis=None, ddof=0)],
        )

        fig.update_layout(
            title="Number of colonies per Hand Sanitizer",
            xaxis_title="Hand Sanitizers",
            yaxis_title="Number of colonies",
            legend_title="Factors",
        )


    return fig


if __name__ == "__main__":
    # read the config file
    ConfigInstance = Config('./config/config.yaml')
    # read DF
    init_df = ConfigInstance.get_init_df()
    #
    init_ques_df = ConfigInstance.get_init_ques_df()
    # read the supported sanitizers list
    supported_sanitizers = ConfigInstance.get_supported_sanitizers()
    print(init_ques_df)
    # create an instance of HandSanitizer Application
    HandSanitizerAppInstance = HandSanitizerApplication(
        init_df, init_ques_df, supported_sanitizers
    )
    Layout(HandSanitizerAppInstance)

    HandSanitizerAppInstance.run()
