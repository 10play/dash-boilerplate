from dash import Dash
import os
import dash_bootstrap_components as dbc
from app import init_app

HOST_PREVIEW = os.environ.get('HOST_PREVIEW', None)
requests_pathname_prefix = HOST_PREVIEW + "/" if HOST_PREVIEW else None
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], title="Boilerplate", suppress_callback_exceptions=True, requests_pathname_prefix=requests_pathname_prefix)
init_app(app)

if __name__ == '__main__':
    app.run_server(debug=True)