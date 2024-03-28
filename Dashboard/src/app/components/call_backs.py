    #     @self._app.dash_app.callback(
    #     Output("content-container1", "children"), [Input("bar_code1", "value")]
    #    )
    #     def update(bar_code1):
    #         return html.Img(
    #             src= self._app.dash_app.get_asset_url("logo.jpg"),
    #             height="300px",
    #         )
    #     @self._app.dash_app.callback(
    #         Output("content-container2", "children"), [Input("bar_code2", "value")]
    #     )
    #     def update(bar_code2):
    #         return html.Img(
    #             src= self._app.dash_app.get_asset_url("lab_pics.jpg"),
    #             height="300px",
    #         )