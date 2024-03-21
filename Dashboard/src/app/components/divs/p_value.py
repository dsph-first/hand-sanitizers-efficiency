from dash import dash, html, Input, Output, callback, Patch, clientside_callback, dcc
import dash_bootstrap_components as dbc


def get_p_value_higher_div(selected_option, stat_value, p_value):
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


def get_p_value_less_div(selected_option, stat_value, p_value):
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
