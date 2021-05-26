from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django_tables2 import RequestConfig
from reportsapp.dash_plotly_repository.geo_plotly_dashboard import createPlotGeo
from reportsapp.dash_plotly_repository.orders_dashboard import createPlotOrders
from reportsapp.database_repository.orders import OrdersRepository
from reportsapp.database_repository.shipping_geography import GeoOrdersRepository
from reportsapp.forms import DayForm, MonthQuaterYearForm
from reportsapp.tabels_repository.tabels import OrdersTab


@require_http_methods(["GET", "POST"])
def total_orders(request):
    form_day = DayForm()
    form_select_month_order_table = MonthQuaterYearForm()
    getItems = OrdersRepository().getAll(min_date='2017-01-01', max_date='2030-12-31')
    rows = OrdersRepository().getBarChart(min_date='2017-01-01', max_date='2030-12-31')
    rows1 = GeoOrdersRepository().getGeoChart()
    table = RequestConfig(request, paginate={"per_page": 10}).configure(OrdersTab(getItems))
    plot_bar = createPlotOrders(rows)[0]
    plot_bar_Wide = createPlotOrders(rows)[1]
    plot_bar_orders = createPlotOrders(rows)[2]
    plot_geo = createPlotGeo(rows1)
    if request.method == 'POST':
        form_day = DayForm(request.POST)
        form_select_month_order_table = MonthQuaterYearForm(request.POST)
        min_date = form_day['min_date_field'].value()
        max_date = form_day['max_date_field'].value()
        if form_select_month_order_table['select'].value() == "miesiące":
            getItems = OrdersRepository().getAllmonth(min_date, max_date)
            form_day = DayForm(request.POST)
            rows = OrdersRepository().getBarChart(min_date, max_date)
            table = RequestConfig(request, paginate={"per_page": 100}).configure(OrdersTab(getItems))
            plot_bar = createPlotOrders(rows)[0]
            plot_bar_Wide = createPlotOrders(rows)[1]
            plot_bar_orders = createPlotOrders(rows)[2]
            return render(request, 'totalorders.html',
                          {"plot": plot_bar, "plot1": plot_bar_Wide,"plot2": plot_bar_orders, "table": table, 'form_day': form_day,
                           'form_select_month_order_table': form_select_month_order_table})
        elif form_select_month_order_table['select'].value() == "kwartały":
            getItems = OrdersRepository().getAllquater(min_date, max_date)
            form_day = DayForm(request.POST)
            rows = OrdersRepository().getBarChartQuater(min_date, max_date)
            table = RequestConfig(request, paginate={"per_page": 100}).configure(OrdersTab(getItems))
            plot_bar = createPlotOrders(rows)[0]
            plot_bar_Wide = createPlotOrders(rows)[1]
            plot_bar_orders = createPlotOrders(rows)[2]
            return render(request, 'totalorders.html',
                          {"plot": plot_bar, "plot1": plot_bar_Wide,"plot2": plot_bar_orders, "table": table, 'form_day': form_day,
                           'form_select_month_order_table': form_select_month_order_table})
        elif form_select_month_order_table['select'].value() == "lata":
            getItems = OrdersRepository().getAllyears(min_date, max_date)
            form_day = DayForm(request.POST)
            rows = OrdersRepository().getBarChartYears(min_date, max_date)
            table = RequestConfig(request, paginate={"per_page": 100}).configure(OrdersTab(getItems))
            plot_bar = createPlotOrders(rows)[0]
            plot_bar_Wide = createPlotOrders(rows)[1]
            plot_bar_orders = createPlotOrders(rows)[2]
            return render(request, 'totalorders.html',
                          {"plot": plot_bar, "plot1": plot_bar_Wide,"plot2": plot_bar_orders, "table": table, 'form_day': form_day,
                           'form_select_month_order_table': form_select_month_order_table})
        elif form_select_month_order_table['select'].value() == "dni":
            getItems = OrdersRepository().getAll(min_date, max_date)
            form_day = DayForm(request.POST)
            rows = OrdersRepository().getBarChartDays(min_date, max_date)
            table = RequestConfig(request, paginate={"per_page": 20}).configure(OrdersTab(getItems))
            plot_bar = createPlotOrders(rows)[0]
            plot_bar_Wide = createPlotOrders(rows)[1]
            plot_bar_orders = createPlotOrders(rows)[2]
            return render(request, 'totalorders.html',
                          {"plot": plot_bar, "plot1": plot_bar_Wide,"plot2": plot_bar_orders, "table": table, 'form_day': form_day,
                           'form_select_month_order_table': form_select_month_order_table})

    return render(request, 'totalorders.html',
                  {"plot": plot_bar, "plot1": plot_bar_Wide, "plot2": plot_bar_orders,"plot_geo": plot_geo, "table": table, 'form_day': form_day,
                   'form_select_month_order_table': form_select_month_order_table})
