from dash import html, dcc
import dash_bootstrap_components as dbc

from config.config import SANITIZERS


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


hs_dropdown = html.Div(
    [
        dbc.Label("Select the non-alcoholic hand-sanitizer"),
        dcc.Dropdown(
            id="hand_sanitizer",
            options=[
                {"label": hand_sanitizers, "value": hand_sanitizers}
                for hand_sanitizers in SANITIZERS
            ],
        ),
    ]
)


controls = dbc.Card(
    [initial_paragraph_content, hs_dropdown],
    body=True,
)
