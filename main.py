from dash.dependencies import Input, Output
from dash import dcc, html, Dash
import dash_bootstrap_components as dbc
from Graph import Graph
from TechnicalIndicators import Moving_Average, Stochastic
from Kraken_data import krakenex_data_import

k, pairs = krakenex_data_import()

try:
    app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

    app.layout = html.Div([
        html.Div(children=[
            html.Label('Select a Pair of Assets', style={'color': 'white'}),
            dcc.Dropdown(pairs, id='demo-dropdown', style={'width': '1000px','color': '#2E8B57'}),

            html.Div(id='dd-output-container')

        ], style={'padding': 10, 'flex': 1}),

        html.Div(children=[

            html.Label('Select the Moving Average', style={'color': 'white'}),
            dcc.Dropdown([10, 20, 30, 40, 50, 60],
                         multi=True, id='average-dropdown', style={'color': '#2E8B57'}),

        ], style={'padding': 10, 'flex': 1}),

        html.Div(children=[

            html.Label('Select the Pair Interval', style={'color': 'white'}),
            dcc.Dropdown([1, 5, 15, 30, 60, 240, 1440, 10080, 21600], 60,
                         multi=False, id='interval-dropdown', style={'color': '#2E8B57'}),

        ], style={'padding': 10, 'flex': 1})
    ], style={'display': 'flex', 'flex-direction': 'row'})


    @app.callback(
        Output('dd-output-container', 'children'),
        [Input('demo-dropdown', 'value'),
         Input('average-dropdown', 'value'),
         Input('interval-dropdown', 'value')]
    )
    def update_figure(value, value_m, value_i):
        try:
            if value is None:
                return ""
            else:
                df, last = k.get_ohlc_data(value, interval=value_i)

                if (value_m is None) == False:
                    for m in value_m:
                        df = Moving_Average(m, df).calculate()
                else:
                    value_m = []

                df = Stochastic(df).calculate()

                return html.Div([
                    dcc.Graph(
                        id='example-graph',
                        figure=Graph(df, value_m, value).graphic)
                ])
        except Exception as e:
            print('This problem has occurred in the figure update: ' + str(e))

except Exception as e:
    print('This problem has occurred with the App design: ' + str(e))

try:
    if __name__ == '__main__':
        app.run_server(debug=True, use_reloader=False)

except Exception as e:
    print('This problem has occurred at the start of the program: ' + str(e))