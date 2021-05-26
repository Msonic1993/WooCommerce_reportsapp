from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django_tables2 import RequestConfig
from reportsapp.dash_plotly_repository.geo_plotly_dashboard import createPlotGeo
from reportsapp.database_repository.shipping_geography import GeoOrdersRepository
from reportsapp.tabels_repository.tabels import GeoOrdersTab


@require_http_methods(["GET", "POST"])
def geo_orders_view(request):
    rows = GeoOrdersRepository().getAll()
    rows1 = GeoOrdersRepository().getGeoChart()
    table = RequestConfig(request, paginate={"per_page": 20}).configure(GeoOrdersTab(rows))
    plot_geo = createPlotGeo(rows1)
    return render(request, 'geoorders.html', {"table": table, 'plot_geo': plot_geo})