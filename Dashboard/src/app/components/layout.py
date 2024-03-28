from dash import dash, html, Input, Output, callback, Patch, clientside_callback, dcc
import dash_bootstrap_components as dbc

from app.components.containers.container import controls


class Layout:
    def __init__(self, handApplication) -> None:
        self._app = handApplication
        self.__init_basic_layout()

        handApplication.init_basic_layout(self.get_basic_layout())

    # ========= Public functions =========

    def show_statistics(self):
        pass

    def get_basic_layout(self):
        return self.__basic_layout

    # ========= Private functions =========

    def __init_basic_layout(self):
        self.__basic_layout = dbc.Container(
            [
                self.__get_navigation_bar(),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                controls,
                            ],
                            width=3,
                        ),
                        dbc.Col(
                            dbc.Card(dbc.Tabs([self.__get_counting_colony_tab(), self.__get_disk_diffusion_tab(),self.__get_rs_seq_tab(),self.__get_user_perceptions_tab()])),
     
                            width=8,
                         
                        ),
                    ]
                ),
            ],
            fluid=True,
            className="dbc dbc-ag-grid",
        )

    def __get_navigation_bar(self):
        self._navigation_bar = dbc.Navbar(
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(
                                    src=self._app.dash_app.get_asset_url("logo.jpg"),
                                    height="30px",
                                )
                            ),
                            dbc.Col(
                                dbc.NavbarBrand("HandSanitizer", className="mr-auto")
                            ),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                    dbc.Collapse(
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                    ),
                ],
                fluid=True,
            ),
            color="dark",
            dark=True,
        )
        return self._navigation_bar

    def __get_counting_colony_tab(self):
        self._counting_colony_tab = dbc.Tab(
            [
                dbc.Row(
                    [
                        html.H4(
                            ("Sample Distribution For counting colony Test"),
                            className="text-center",
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
                        html.H4(("Statistical Analysis"), className="text-center"),
                        
                        dbc.Row(
                            [
                                dbc.Row(
                                    [
                                        dcc.RadioItems(
                                            id="radio-selector",
                                            options=[
                                                {
                                                    "label": [
                                                        html.Span('Mann-Whitney U')
                                                    ],
                                                    "value": 'Mann-Whitney U',
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
            label="Counting Colony",
        )
        return self._counting_colony_tab

    def __get_disk_diffusion_tab(self):
        self._disk_diffusion_tab = dbc.Tab(
            [
                dbc.Row(
                    [
                        html.H4(
                            ("Sample Distribution For disk Diffusion Test"),
                            className="text-center",
                        ),
                        dbc.Col(),
                    ]
                ),
                dbc.Row(
                    [
                        html.H4(("Statistical Analysis"), className="text-center"),
                        dbc.Row(
                            [
                                dbc.Row([]),
                                dbc.Row([]),
                            ]
                        ),
                    ]
                ),
            ],
            label="Disk Diffusion Test",
        )
        return self._disk_diffusion_tab

    def __get_rs_seq_tab(self):
        self._rs_seq_tab = dbc.Tab(
            [
                dbc.Row(
                    [
                        html.H4(
                            ("Sample Distribution For 16RS Sequencing Test"),
                            className="text-center",
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        html.H4(("Statistical Analysis"), className="text-center"),
                        dbc.Row(
                            [
                                dbc.Row([]),
                                dbc.Row([]),
                            ]
                        ),
                    ]
                ),
            ],
            label="16rs Sequencing",
            id="sequencing",
        )
        return self._rs_seq_tab

    def __get_user_perceptions_tab(self):
        self._user_perceptions_tab = dbc.Tab(
            [
                dbc.Row(
                    [
                        html.H4(
                            ("Sample Distribution For User Perception Test"),
                            className="text-center",
                        ),
                        dbc.Col(),
                    ]
                ),
                dbc.Row(
                    [
                        html.H4(("Statistical Analysis"), className="text-center"),
                        dbc.Row(
                            [
                                dbc.Row([]),
                                dbc.Row([]),
                            ]
                        ),
                    ]
                ),
            ],
            label="User perception",
            id="user_perception",
        )
        return self._user_perceptions_tab
