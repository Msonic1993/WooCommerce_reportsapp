import datetime
import json
import locale
from time import strptime
import plotly.express as px
import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.figure_factory import np


def createPlotTopProducts(getItems):
    df = pd.DataFrame(getItems, columns=['date', 'name', 'quantity', 'value'])

    if len(df.values) == 0:
        fig = px.line(df, x='date', y='quantity').update_traces(mode='lines+markers')
    else:
        fig = px.line(df, x='date', y='quantity', color='name').update_traces(mode='lines+markers')
    fig.update_xaxes(title_text='Miesiące')
    fig.update_yaxes(title_text='Ilość zamówień')
    fig.update_layout(showlegend=True)
    fig.update_xaxes(

        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON