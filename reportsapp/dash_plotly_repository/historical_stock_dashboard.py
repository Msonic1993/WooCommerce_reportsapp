import datetime
import json
import locale
from time import strptime
import plotly.express as px
import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.figure_factory import np


def createPlotHistoricalStock(getItems_historical):
    df = pd.DataFrame(getItems_historical, columns=['date', 'product_name','product_category', 'quantity','net_price','stock_value'])
    if len(df.values) == 0:
        fig = px.line(df, x='date', y='quantity', labels={'date':'Data', 'quantity':'Ilość na stanie','product_name':'Nazwa produktu'}).update_traces(mode='lines+markers')
    else:
        fig = px.line(df, x='date', y='quantity', color='product_name',labels={'date':'Data', 'quantity':'Ilość na stanie','product_name':'Nazwa produktu'}).update_traces(mode='lines+markers')
    fig.update_xaxes(title_text='Data')
    fig.update_yaxes(title_text='Ilość na stanie')
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