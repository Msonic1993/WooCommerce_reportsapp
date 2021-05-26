from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django_tables2 import RequestConfig
from reportsapp.database_repository.incomevsexpenses import IncomeVsExpensesRepository
from reportsapp.forms import MonthForm, DayForm
from reportsapp.tabels_repository.tabels import IncomeVsExpensesTab, MarginValueTab


@require_http_methods(["GET", "POST"])
def income_expenses(request):
    form = MonthForm()
    getItems = IncomeVsExpensesRepository().getAll(min_date='2000-01', max_date='2050-12')
    getItemsMarginValue = IncomeVsExpensesRepository().getAllmargin()
    # rows = OrdersRepository().getBarChart()
    table = RequestConfig(request).configure(IncomeVsExpensesTab(getItems))
    table_margin_value = MarginValueTab(getItemsMarginValue)
    # plot_bar = income_table()
    # plot_bar_Wide = createPlotOrders(rows)[1]
    if request.method == 'POST':
        form = DayForm(request.POST)
        min_date = form['min_date_field'].value()
        max_date = form['max_date_field'].value()
        getItems = IncomeVsExpensesRepository().getAll(min_date, max_date)
        getItemsMarginValue = IncomeVsExpensesRepository().getAllmargin()
        form = MonthForm(request.POST)
        # rows = OrdersRepository().getBarChart()
        table = IncomeVsExpensesTab(getItems)
        table_margin_value = MarginValueTab(getItemsMarginValue)
        # plot_bar = income_table()
        # plot_bar_Wide = createPlotOrders(rows)[1]
        return render(request, 'incomevsexpenses.html',
                      {"table": table, "table_margin_value": table_margin_value, 'form': form})
    return render(request, 'incomevsexpenses.html',
                  {"table": table, "table_margin_value": table_margin_value, 'form': form})
