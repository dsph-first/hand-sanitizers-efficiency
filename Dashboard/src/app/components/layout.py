from dash import dash, html, Input, Output, callback, Patch, clientside_callback, dcc
import dash_bootstrap_components as dbc

from app.components.containers.container import controls
from app.modules.questionaries import map_ratings_to_scale

global bar_codes
bar_codes = ["barcode1", "barcode 2"]


class Layout:
    def __init__(self, handApplication) -> None:
        self._app = handApplication
        self.__init_basic_layout()

        handApplication.init_basic_layout(self.get_basic_layout())

        # self.register_callback()
    # ========= Public functions =========
        
    # ========= Callbacks =========
    def barcode1_callback(self):
        @self._app.dash_app.callback(
        Output("content-container1", "children"), [Input("bar_code1", "value")]
       )
        def update(bar_code1):
            if bar_code1== "" or bar_code1 == None:
                     return html.Div()

            if bar_code1!= None:
                return html.Img(
                    src= self._app.dash_app.get_asset_url("logo.jpg"),
                    height="300px",
                )
    def barcode2_callback(self):
        @self._app.dash_app.callback(
            Output("content-container2", "children"), [Input("bar_code2", "value")]
        )
        def update(bar_code2):
            if bar_code2== "" or bar_code2 == None:
                     return html.Div()

            if bar_code2!= None:
                    
                return html.Img(
                    src= self._app.dash_app.get_asset_url("lab_pics.jpg"),
                    height="300px",
                )
            

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
                            dbc.Card(
                                dbc.Tabs(
                                    [
                                        self.__get_counting_colony_tab(),
                                        self.__get_disk_diffusion_tab(),
                                        self.__get_rs_seq_tab(),
                                        self.__get_user_perceptions_tab(),
                                    ]
                                )
                            ),
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
                        dbc.Col(
                            dbc.Row(
                                [
                                    html.H4(
                                        ("Fingertip Experiment Results"),
                                        className="text-center",
                                    ),
                                    dbc.Card(
                                        [
                                            dcc.Graph(
                                                id="bar_graph",
                                                figure={},
                                                # className="h-100",
                                            ),
                                        ]
                                    ),
                                ]
                            ),
                            # lg=6,
                        ),
                        dbc.Col(
                            dbc.Row(
                                [
                                    html.H4(
                                        "Pictures of growing colonies",
                                        className="text-center",
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                            [
                                                html.H4(
                                                    "Control",
                                                    className="card-title",
                                                ),
                                                html.Img(
                                                    src=self._app.dash_app.get_asset_url(
                                                        "lab_pic_control.jpg"
                                                    ),
                                                    height="400px",
                                                ),
                                            ]
                                        ),
                                        lg=6,
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                            [
                                                html.H4(
                                                    "Hand sanitizer",
                                                    className="card-title",
                                                ),
                                                html.Img(
                                                    src=self._app.dash_app.get_asset_url(
                                                        "lab_pic_handsanitizer.jpg"
                                                    ),
                                                    height="400px",
                                                ),
                                            ]
                                        ),
                                        lg=6,
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        html.Br(),
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
                                                        html.Span("Mann-Whitney U")
                                                    ],
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
                        dbc.Col(
                            [   self.barcode1_callback(),
                                dbc.Label("Select the bar code group 1"),
                                dcc.Dropdown(
                                    id="bar_code1",
                                    options=[
                                        {"label": bar_code, "value": bar_code}
                                        for bar_code in bar_codes
                                    ],
                                ),
                                html.Div(id="content-container1"),
                            ]
                        ),
                        dbc.Col(
                            [   self.barcode2_callback(),
                                dbc.Label("Select the bar code group 2"),
                                dcc.Dropdown(
                                    id="bar_code2",
                                    options=[
                                        {"label": bar_code, "value": bar_code}
                                        for bar_code in bar_codes
                                    ],
                                ),
                                html.Div(id="content-container2"),
                            ]
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
                        data = self._app.get_ques_df(), 
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


