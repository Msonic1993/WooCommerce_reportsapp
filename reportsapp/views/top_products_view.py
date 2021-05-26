from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django_tables2 import RequestConfig
from reportsapp.dash_plotly_repository.top_products_dashboard import createPlotTopProducts
from reportsapp.database_repository.bestproducts import TopProductsRepository
from reportsapp.database_repository.products import ProductsRepository
from reportsapp.forms import MonthForm, StartPartneredDeliveryForm, DayForm
from reportsapp.tabels_repository.tabels import BestProductTab, BestProductAllTab


@require_http_methods(["GET", "POST"])
def top_products(request):
    form = MonthForm()
    rows_products = ProductsRepository().getAll()
    get_product_name = StartPartneredDeliveryForm(rows_products)
    getItems = TopProductsRepository().getAll(min_date='2000-01', max_date='2050-12', get_product_name="%%")
    get_items_all = TopProductsRepository().getAllDate()
    plot_line = createPlotTopProducts(getItems)
    table = RequestConfig(request, paginate={"per_page": 10}).configure(BestProductTab(getItems))
    table_all_time = RequestConfig(request, paginate={"per_page": 10}).configure(BestProductAllTab(get_items_all))
    # plot_bar = income_table()
    # plot_bar_Wide = createPlotOrders(rows)[1]
    if request.method == 'POST':
        form = DayForm(request.POST)
        get_product_name = request.POST['browser']
        min_date = form['min_date_field'].value()
        max_date = form['max_date_field'].value()
        getItems = TopProductsRepository().getAll(min_date, max_date, get_product_name)
        get_items_all = TopProductsRepository().getAllDate()
        form = MonthForm(request.POST)
        get_product_name1 = StartPartneredDeliveryForm(rows_products)
        table = RequestConfig(request, paginate={"per_page": 100}).configure(BestProductTab(getItems))
        table_all_time = RequestConfig(request, paginate={"per_page": 10}).configure(BestProductAllTab(get_items_all))
        plot_line = createPlotTopProducts(getItems)
        # plot_bar_Wide = createPlotOrders(rows)[1]
        return render(request, 'bestproducts.html',
                      {"table": table, "table_all_time": table_all_time, 'form': form, 'plot_line': plot_line,
                       'get_product_name': get_product_name1})

    return render(request, 'bestproducts.html',
                  {"table": table, "table_all_time": table_all_time, 'form': form, 'get_product_name': get_product_name,
                   'plot_line': plot_line})
