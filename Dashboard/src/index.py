
"""This module is full working module before adding the tabs"""

from dash import dash, html, Input, Output, callback, Patch, clientside_callback, dcc
import plotly.express as px
import pandas as pd
import logging

from app.app import HandSanitizerApplication
from config.config import get_config

global HandSanitizerAppInstance


def calculate_handle_sanitzer_stats(sanitizer_name):
    print(
        f'calculate_handle_sanitzer_stats::sanitizer: {sanitizer_name}'
    )
    # log = logging.Logger(level="DEBUG")
    # log.info(
    #     f'calculate_handle_sanitzer_stats::sanitizer: ${sanitizer_name}'
    # )


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
    fig = None
    if hand_sanitizer != None:
        # calculate_handle_sanitzer_stats(hand_sanitizer)
        # print the hand sanitizer stats:
        # - p_value
        # HandSanitizerAppInstance.get_two_sample_ttest()
        df = HandSanitizerAppInstance.get_df_for(hand_sanitizer)
        fig = px.bar(
            df,
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


def list_to_bool_dic(lst):
    res_dict = {}
    for i in range(0, len(lst), 1):
        res_dict[lst[i]] = True
    return res_dict


if __name__ == "__main__":
    # read the config file
    config = get_config('./config/config.yaml')

    # read DF
    init_df = pd.read_excel(config['data_path'])
    # read the supported sanitizers list
    supported_sanitizers = list_to_bool_dic(config['supported_sanitizers'])

    # create an instance of HandSanitizer Application
    HandSanitizerAppInstance = HandSanitizerApplication(
        init_df, supported_sanitizers
    )

    HandSanitizerAppInstance.run()
