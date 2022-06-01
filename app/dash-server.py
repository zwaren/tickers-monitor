import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from db import db
from models import TickerChange

app = Dash(__name__)
ticker_codes = TickerChange.objects_in(db).only('ticker_code').distinct()

app.layout = html.Div([
    dcc.Dropdown(
        options=[ticker_code.ticker_code for ticker_code in ticker_codes],
        value=ticker_codes[0].ticker_code,
        id='ticker-select',
    ),
    dcc.Graph(id='ticker-graph'),
    dcc.Interval(
        id='interval-component',
        interval=1 * 1000,
        n_intervals=0
    ),
])


@app.callback(
    Output('ticker-graph', 'figure'),
    Input('interval-component', 'n_intervals'),
    Input('ticker-select', 'value'),
)
def update_graph(n, value):
    ticker_changes = TickerChange.objects_in(db).filter(TickerChange.ticker_code == value).order_by('timestamp')
    timestamps = [ts.timestamp for ts in ticker_changes.only('timestamp')]
    prices = [price.current_price for price in ticker_changes.only('current_price')]

    fig = go.Figure([go.Scatter(x=timestamps, y=prices)])
    return fig


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
