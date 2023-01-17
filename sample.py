import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = pd.read_csv("data.csv")
data["ti"] = pd.to_datetime(data["ti"])

# print(filtered_data[['ti', 'repo', 'jobs', 'status', 'exp', 'sum', '%Failure']])
# jobs = filtered_data['jobs'].sum()
# unique_metrics = filtered_data['repo'].unique()
#
# jobs = filtered_data['%Failure'].sum()
# print(jobs, unique_metrics)

app.layout = html.Div(
    id="app-container",
    children=[
        html.Div(
            id="header-area",
            children=[
                html.H1(
                    id="header-title",
                    children="Status Dashboard",

                ),
                # html.P(
                #     id="header-description",
                #     children=("The cost of precious metals", html.Br(), "between 2018 and 2021"),
                # ),
            ],
        ),
        html.Div(
            id="menu-area",
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className="menu-title",
                            children="Metrics"
                        ),
                        dcc.Dropdown(
                            id="metrics",
                            className="dropdown",
                            options=[
                                {'label': 'Repository', 'value': 'repo'},
                                {'label': 'Measurement Type', 'value': 'measurement_type'},
                                {'label': 'Data Type', 'value': 'data_type'}],
                            value='repo',
                            clearable=False,
                        )
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(
                            className="menu-title",
                            children="Date Range"
                        ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=data.ti.min().date(),
                            max_date_allowed=data.ti.max().date(),
                            start_date=data.ti.min().date(),
                            end_date=data.ti.max().date()
                        )
                    ]
                )
            ]
        ),
        html.Div(id='output-1'),
    ]
)

@app.callback(
    Output(component_id='output-1', component_property='children'),
    [
        Input(component_id='metrics', component_property='value'),
        Input("date-range", "start_date"),
        Input("date-range", "end_date")
    ]
)
def update_output(metrics, start_date, end_date):
    filtered_data = data.loc[(data.ti >= start_date) & (data.ti <= end_date)]

    return html.Div([
    html.H4('Summary', className='mt-5 mb-2'),
    html.Table([
        html.Thead([
            html.Tr([
                html.Th('Parameter', className='text-center'),
                html.Th('Jobs', className='text-center'),
                html.Th('Sparkline', className='text-center'),
                html.Th('Failure%', className='text-center'),
                html.Th('Failure vs Pass', className='text-center')
            ])
        ], className='thead-dark mb-5'),
        html.Tbody([
            html.Tr([
                html.Td(metrics, className='text-center'),
                html.Td(start_date, className='text-center'),
                html.Td(dcc.Graph(id='sparkline-chart',
                                  figure={'data':
                                              [
                                                  {'x': [2,4,5],
                                                   'y': [4, 1, 2],
                                                   'type': 'line', 'name': 'SF'
                                                   }
                                              ]
                                  })
                        ),
                html.Td(end_date, className='text-center'),
                html.Td(dcc.Graph(id='bar-chart',
                                  figure=
                                    {'data':
                                         [
                                             {'x': [1, 2, 3],
                                              'y': [4, 1, 2],
                                              'type': 'bar', 'name': 'SF'
                                              }
                                         ]
                                    },
                                  ),
                        ),
            ])
        ])
    ], className='table table-dark table-striped')
], className='container')

if __name__ == '__main__':
    app.run_server(debug=True)