import dash_bootstrap_components as dbc

import app.components.nav_bars.navigation_bar as navig_bar
from app.components.containers.container import controls
from app.components.tabs import counting_colony_tab as cc, disk_diffusion_tab as dd, rs_seq_tab as seq, user_perceptions_tab as up


tabs = dbc.Card(dbc.Tabs([cc.counting_colony_tab,dd.disk_diffusion_tab, seq.rs_seq_tab,up.user_perceptions_tab]))