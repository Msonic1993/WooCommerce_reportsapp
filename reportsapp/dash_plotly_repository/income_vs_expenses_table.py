# import json
#
# import plotly.express as px
# import pandas as pd
# import plotly
# import plotly.graph_objs as go
#
#
#
# def income_table():
#     colors = ['rgb(239, 243, 255)', 'rgb(189, 215, 231)', 'rgb(107, 174, 214)',
#               'rgb(49, 130, 189)', 'rgb(8, 81, 156)']
#     data = IncomeVsExpensesRepository().getAll()
#     df = pd.DataFrame(data)
#
#     fig = go.Figure(data=[go.Table(
#       header=dict(
#         values=["Color", "<b>YEAR</b>"],
#         line_color='white', fill_color='white',
#         align='center', font=dict(color='black', size=12)
#       ),
#       cells=dict(
#         values=[df.date, df._sum_total_sales, df.total_buy, df.wynik],
#         align='center', font=dict(color='black', size=11)
#       ))
#     ])
#
#     graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#
#     return graphJSON