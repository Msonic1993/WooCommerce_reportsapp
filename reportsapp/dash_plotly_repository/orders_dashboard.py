
import json
import plotly.express as px
import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots


def createPlotOrders(rows):

    df = pd.DataFrame(rows, columns=['Data zamówienia', 'Ilość produktów',  'ilość zamówień','Wartość netto', 'wartość VAT', 'Wartość brutto'])

    fig = px.bar(df, y='Ilość produktów', x='Data zamówienia', text='Ilość produktów',color='Wartość netto')
    fig.update_traces(textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide',barmode='group', hovermode='x',title_text="Wykres ilość produktów")

    fig1 =  go.Figure(data=[
    go.Bar(name='Wartość netto', x=df['Data zamówienia'], y=round(df['Wartość netto'],2),text=round(df['Wartość netto'],2),textposition='auto'),
    go.Bar(name='Wartość brutto', x=df['Data zamówienia'], y=round(df['Wartość brutto'],2),text=round(df['Wartość brutto'],2),textposition='auto')
])


    fig2 = make_subplots(specs=[[{"secondary_y": True}]])

    fig2.add_trace(
        go.Bar(name='Ilość zamówień', x=df['Data zamówienia'], y=df['ilość zamówień'],text=df['ilość zamówień'],textposition='auto'),
        secondary_y=False,
    )

    fig2.add_trace(
        go.Scatter(name='Wartość netto', x=df['Data zamówienia'], y=round(df['Wartość netto']),text=round(df['Wartość netto'],2),textposition='top right',
                  textfont=dict(color='#212529'),
                  mode='lines+markers+text',
                  marker=dict(color='#dc3545', size=7),
                  line=dict(color='#dc3545', width=1, dash='dash')),
        secondary_y=True,
    )
    fig2.update_layout(
        title_text="Dwuwymiarowy wykres wartości zamówień netto oraz ilości zamówień"
    )

    fig2.update_xaxes(title_text="Data")

    fig2.update_yaxes(title_text="<b>Zamówienia</b> ilość", secondary_y=False)
    fig2.update_yaxes(title_text="<b>Wartość</b> netto", secondary_y=True)

    fig1.update_layout(barmode='group', hovermode='x',title_text="Wykres wartości zamówień")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON, graphJSON1,graphJSON2