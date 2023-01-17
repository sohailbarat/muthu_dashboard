data = pd.read_csv("data.csv")
data["ti"] = pd.to_datetime(data["ti"])
filtered_data = data.loc[(data.ti >= '2022-01-01') & (data.ti <= '2023-01-01')]
grouped_data = filtered_data.groupby('repo')

jobs = grouped_data['jobs'].sum()
failure = grouped_data['%Failure'].sum()

group_by_ti = filtered_data.groupby('ti')

# failure = jobs['%Failure']
print(jobs, failure, group_by_ti.groups)

# import dash
# from dash import dcc
# from dash import html
# from dash.dependencies import Output, Input
# import plotly.express as px
# import pandas as pd
#
# # Read in the data
# data = pd.read_csv("data.csv")
# data["ti"] = pd.to_datetime(data["ti"])
#
# # Create a plotly plot for use by dcc.Graph().
# # fig = px.line(
# #     data,
# #     title="Precious Metal Prices 2018-2021",
# #     x="DateTime",
# #     y=["Gold"],
# #     color_discrete_map={"Gold": "gold"}
# # )
#
# app = dash.Dash(__name__)
# app.title = "Precious Metal Prices 2018-2021"
#
# app.layout = html.Div(
#     id="app-container",
#     children=[
#         html.Div(
#             id="header-area",
#             children=[
#                 html.H1(
#                     id="header-title",
#                     children="Precious Metal Prices",
#
#                 ),
#                 html.P(
#                     id="header-description",
#                     children=("The cost of precious metals", html.Br(), "between 2018 and 2021"),
#                 ),
#             ],
#         ),
#         html.Div(
#             id="menu-area",
#             children=[
#                 html.Div(
#                     children=[
#                         html.Div(
#                             className="menu-title",
#                             children="Metal"
#                         ),
#                         dcc.Dropdown(
#                             id="metal-filter",
#                             className="dropdown",
#                             options=[
#                                 {'label': 'Repository', 'value': 'repo'},
#                                 {'label': 'Measurement Type', 'value': 'measurement_type'},
#                                 {'label': 'Data Type', 'value': 'data_type'}],
#                             value='repo',
#                             clearable=False,
#                         )
#                     ]
#                 ),
#                 html.Div(
#                     children=[
#                         html.Div(
#                             className="menu-title",
#                             children="Date Range"
#                         ),
#                         dcc.DatePickerRange(
#                             id="date-range",
#                             min_date_allowed=data.ti.min().date(),
#                             max_date_allowed=data.ti.max().date(),
#                             start_date=data.ti.min().date(),
#                             end_date=data.ti.max().date()
#                         )
#                     ]
#                 )
#             ]
#         ),
#         # html.Div(
#         #     id="graph-container",
#         #     children=
#         #         [
#         #             dcc.Graph(
#         #                 id="price-chart",
#         #                 # figure=fig,
#         #                 # config={"displayModeBar": False}
#         #             ),
#         #         ]
#         # ),
#         html.Div(id='output-1'),
#     ]
# )
#
#
# @app.callback(
#     [
#         # Output("price-chart", "figure"),
#         Output("output-1", "children"),
#     ],
#     [
#         Input("metal-filter", "value"),
#         Input("date-range", "start_date"),
#         Input("date-range", "end_date")
#     ]
# )
# def update_chart(metal, start_date, end_date):
#     filtered_data = data.loc[(data.ti >= start_date) & (data.ti <= end_date)]
#
#     # return start_date
#     return html.H1(children="adads")
#     #     , {
#     #     'data': [{'x': [1, 2, 3], 'y': [4, 1, 2]}],
#     #     'layout': {'title': start_date}
#     # }
#
#     # Create a plotly plot for use by dcc.Graph().
#     # fig = px.line(
#     #     filtered_data,
#     #     title="Precious Metal Prices 2018-2021",
#     #     x="DateTime",
#     #     y=[metal],
#     #     color_discrete_map={
#     #         "Platinum": "#E5E4E2",
#     #         "Gold": "gold",
#     #         "Silver": "silver",
#     #         "Palladium": "#CED0DD",
#     #         "Rhodium": "#E2E7E1",
#     #         "Iridium": "#3D3C3A",
#     #         "Ruthenium": "#C9CBC8"
#     #     }
#     # )
#     #
#     # fig.update_layout(
#     #     template="plotly_dark",
#     #     xaxis_title="Date",
#     #     yaxis_title="Price (USD/oz)",
#     #     font=dict(
#     #         family="Verdana, sans-serif",
#     #         size=18,
#     #         color="white"
#     #     ),
#     # )
#     #
#     # return fig
#
#
# if __name__ == "__main__":
#     app.run_server(debug=True, port=8052)
