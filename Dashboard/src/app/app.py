from dash import dash, Input, Output, callback, Patch, clientside_callback
import dash_bootstrap_components as dbc
import pandas as pd

from app.modules.statistics_analysis import stat_analysis
from app.modules.data_processing import cleaup_df
from app.components.layout import basic_layout


DBC_CSS = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css"


class HandSanitizerApplication:
    def __init__(self, init_df, supported_sanitizers) -> None:
        #
        self.dash_app = dash.Dash(__name__, external_stylesheets=[
            dbc.themes.BOOTSTRAP, (DBC_CSS)]
        )
        #
        self._df = self.__init_df(init_df)
        #
        self._hand_sanitizers = supported_sanitizers
        #
        self.__init_basic_layout()

    # ========= Public functions =========

    def get_df(self) -> pd.DataFrame:
        return self._df

    def get_df_for(self, sanitizer_name) -> pd.DataFrame:
        if self.__is_sanitizer_exists(sanitizer_name) != True:
            return None

        print(self._df[self._df['HS'] == sanitizer_name])
        return self._df[self._df['HS'] == sanitizer_name]

    def set_df(self, new_df):
        self._df = new_df

    # TODO
    def print_sanitizer_properties(self, sanitizer_name):
        if self.__is_sanitizer_exists(sanitizer_name) != True:
            return None
        pass

    def run(self):
        self.dash_app.run_server(debug=True, use_reloader=True)

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

    def __init_basic_layout(self):
        self.dash_app.layout = basic_layout

    def __calculate_stats(self, stat_model_name):
        stat_value, p_value = stat_analysis(stat_model_name, self._df)
        print("STATS: ", stat_value, p_value)
        if stat_value == None or p_value == None:
            return
        if p_value > 0.05:
            p_value = "{0:.4f}".format(p_value)
            stat_value = "{0:.4f}".format(stat_value)
            print(">0.05")
        #  return get_p_value_div_higher(selected_option, stat_value, p_value)
        if p_value < 0.05:
            p_value = "{0:.2f}".format(p_value)
            stat_value = str(stat_value)
        print("<0.05")
