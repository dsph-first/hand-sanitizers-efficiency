from dash import dash, Input, Output, callback, Patch, clientside_callback
import dash_bootstrap_components as dbc
import pandas as pd

from app.modules.statistics_analysis import stat_analysis, normality_check
from app.modules.data_processing import cleaup_df

import os

assets_path= os.getcwd() + '/public/assets'

DBC_CSS = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css"


class HandSanitizerApplication:
    def __init__(self, init_df, supported_sanitizers) -> None:

        self.dash_app = dash.Dash(__name__, external_stylesheets=[
            dbc.themes.BOOTSTRAP, (DBC_CSS)], assets_folder = assets_path
        )

        self._df = self.__init_df(init_df)

        self._hand_sanitizers = supported_sanitizers

    # ========= Public functions =========

    def init_basic_layout(self, basic_layout):
        self.dash_app.layout = basic_layout

    def run(self):
        self.dash_app.run_server(debug=True, use_reloader=True)

    def get_df(self) -> pd.DataFrame:
        return self._df

    def set_df(self, new_df):
        self._df = new_df

    def get_df_for(self, sanitizer_name) -> pd.DataFrame:
        if self.__is_sanitizer_exists(sanitizer_name) != True:
            return None
        df = self._df[self._df['HS'] == sanitizer_name]
        self.set_df(df)
        return df

    # TODO
    def print_sanitizer_properties(self, sanitizer_name):
        if self.__is_sanitizer_exists(sanitizer_name) != True:
            return None
        pass

    # Distribution Check
    def check_distribution(self):
        return self.__calculate_distribution()

    def calculate_stats_for_model(self, method_name):
        return self.__calculate_stats(method_name)

    def get_two_sample_ttest(self):
        self.__calculate_stats('Two-sample t-test')

    # TODO
    def get_another_sample_ttest(self):
        self.__calculate_stats('Two-sample t-test')

    # ========= Private functions =========

    def __init_df(self, new_df) -> pd.DataFrame:
        return cleaup_df(new_df)

    def __is_sanitizer_exists(self, sanitizer_name) -> bool:
        return self._hand_sanitizers[sanitizer_name]

    def __calculate_stats(self, stat_model_name):
        return stat_analysis(stat_model_name, self._df)

    def __calculate_distribution(self):
        # df = self._df
        return normality_check(self._df)
