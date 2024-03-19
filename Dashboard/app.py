from dash import dash, html, Input, Output, callback, Patch, clientside_callback
import dash_bootstrap_components as dbc


dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])

server = app.server

