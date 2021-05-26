import json

import plotly.express as px
import pandas as pd
import plotly
import plotly.graph_objs as go



def createPlotCosts(rows):

    df = pd.DataFrame(rows,columns=['cost_name','date_cost', 'num_items_buy', 'unit_price', 'Wartość podatku Vat', 'Koszty transportu','shipping_per_unit', 'Koszty Netto', 'total_buy', 'unit_cost','unit_cost_pln'])
    fig1 = px.bar(df, x='date_cost', y=['Wartość podatku Vat','Koszty transportu', 'Koszty Netto'], title="Wykres przedstawia koszty netto wraz z dostawą i podatkiem ", barmode='relative')

    graphJSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)


    return graphJSON