import json
import datetime
import json
import locale
from time import strptime

import plotly.express as px
import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.graph_objects as go

import pandas as pd

def createPlotGeo(rows1):

    df = pd.DataFrame(rows1, columns=['id','meta_key', 'city', 'ilosc', 'wartosc'])

    fig = px.scatter(df, x="wartosc", y="ilosc",
                     size="wartosc", color="ilosc",
                     hover_name="city", log_x=True, size_max=60,title="Prezentacja danych na wykresie")
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', barmode='group', hovermode='x')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON