from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django_tables2 import RequestConfig
from reportsapp.dash_plotly_repository.historical_stock_dashboard import createPlotHistoricalStock
from reportsapp.database_repository.products import ProductsRepository
from reportsapp.database_repository.warehouse import WarehouseRepository
from reportsapp.forms import MonthForm, StartPartneredDeliveryForm
from reportsapp.tabels_repository.tabels import WarehouseTab, WarehouseHistoricalTab


@require_http_methods(["GET", "POST"])
def warehouse_view(request):
    CalendarForm = MonthForm()
    rows_products = ProductsRepository().getAll()
    get_product_name = StartPartneredDeliveryForm(rows_products)
    getItems = WarehouseRepository().getAll()[0]
    getItems_historical = WarehouseRepository().getAllLocalDB()
    form = MonthForm(request.POST)
    table = RequestConfig(request, paginate={"per_page": 20}).configure(WarehouseTab(getItems))
    table_historical = RequestConfig(request, paginate={"per_page": 20}).configure(
        WarehouseHistoricalTab(getItems_historical))
    plot_line = createPlotHistoricalStock(getItems_historical)
    if request.method == 'POST':
        CalendarForm = MonthForm(request.POST)
        min_date = form['min_date_field'].value()
        max_date = form['max_date_field'].value()
        get_product_name = request.POST['browser']
        getItems = WarehouseRepository().getOne(get_product_name)
        getItems_historical = WarehouseRepository().getOneLocalDB(get_product_name)
        form = MonthForm(request.POST)
        table = RequestConfig(request, paginate={"per_page": 20}).configure(WarehouseTab(getItems))
        table_historical = RequestConfig(request, paginate={"per_page": 20}).configure(
            WarehouseHistoricalTab(getItems_historical))
        plot_line = createPlotHistoricalStock(getItems_historical)
        return render(request, 'warehouse.html',
                      {"table": table, 'table_historical': table_historical, 'get_product_name': get_product_name,
                       'plot_line': plot_line})

    return render(request, 'warehouse.html',
                  {"table": table, 'table_historical': table_historical, 'get_product_name': get_product_name,
                   'plot_line': plot_line})
