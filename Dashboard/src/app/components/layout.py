from dash import dash, html, Input, Output, callback, Patch, clientside_callback, dcc
import dash_bootstrap_components as dbc

import app.components.nav_bars.navigation_bar as navig_bar
from app.components.containers.container import controls

# Tabs
from app.components.tabs.basic_tabs import tabs


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
                            [
                                tabs
                            ], width=8,
                            # fluid=True,
                        ),
                    ]
                ),
            ],
            fluid=True,
            className="dbc dbc-ag-grid",
        )

    def __get_navigation_bar(self):
        print('ASSET PATH: ', self._app.get_asset_url())
        self._navigation_bar = dbc.Navbar(
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(src=self._app.get_asset_url(), height='30px')),
                            dbc.Col(dbc.NavbarBrand(
                                'HandSanitizer', className='mr-auto')),
                        ],
                        align='center',
                        className='g-0',
                    ),
                    dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                    dbc.Collapse(
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                    ),
                ],
                fluid=True
            ),
            color="dark",
            dark=True,
        )
        return self._navigation_bar
