
"""
Script to embed krona html reports in a dash app

References:
    https://github.com/plotly/dash-docs/issues/1068. github: joelostblom
    https://stackoverflow.com/questions/64736956/how-to-use-iframe-in-dash-plotly-python-html. stackoverflow: ehmer
    https://community.plotly.com/t/including-html-plotly-graphs-in-dash-app/35180/3
    
"""

import os
import threading
import yaml
from dash import Dash, html, dcc, Output, Input
from flask import Flask, send_from_directory

with open("config.yaml", "r") as config_file:
    config = yaml.load(config_file)

# Directory where the reports are located
report_dir = config["report_dir"]
html_files_dir = config["html_dir"]


# Initialize Flask app
app = Flask(__name__)

# Route to serve HTML files
@app.route('/<path:filename>')
def serve_html(filename):
    """Serve HTML files from the specified directory."""
    html_dir = os.path.join(os.getcwd(), html_dir)
    return send_from_directory(html_dir, filename)

def generate_options(report_dir):
    """Generate dropdown options and corresponding report filenames."""
    files = os.listdir(report_dir)
    files.sort()
    options = [{"label": f"Microbial abundance bracken - barcode {i}",
                "value": f"report{i}"} for i in range(len(files))]
    reports = {f"report{i}": file for i, file in enumerate(files)}
    return options, reports

# Generate options and report dictionary
options_1, reports_1 = generate_options(report_dir)

# Initialize Dash app
dashapp = Dash(__name__)

# Layout of the Dash app
dashapp.layout = html.Div([
    html.Div(id='target'),
    dcc.Dropdown(
        id='dropdown',
        options=options_1,
        value='report0'
    )
])

# Callback function to embed iframe based on dropdown selection
# Output to 'target' div in layout dash app
# Iframe -> krona report is a html file
@dashapp.callback(Output('target', 'children'), [Input('dropdown', 'value')])
def embed_iframe(value):
    """Embed iframe to display selected report."""
    global reports_1
    reports = reports_1
    file_name = reports.get(value)
    if file_name:
        return html.Iframe(src=f'http://127.0.0.1:5000/krona/reports/{file_name}',
                           style={"height": "800px", "width": "100%"})
    else:
        return "Selected report not found."

if __name__ == '__main__':
    # Run Flask app in a separate thread
    file_server = threading.Thread(target=dashapp.run_server)
    file_server.start()
    # Run Flask app
    app.run()
