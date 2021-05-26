from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django_tables2 import RequestConfig
from reportsapp.database_repository.fixedcosts import FixedCostsRepository
from reportsapp.forms import FixedCostsForm, DayForm, MonthForm
from reportsapp.tabels_repository.tabels import FixedCostsTab


@require_http_methods(["GET", "POST"])
def fixed_costs(request):
    form1 = FixedCostsForm()
    form = DayForm()
    getItems = FixedCostsRepository().getAll(min_date='2000-01-01', max_date='2050-12-31')
    table = RequestConfig(request, paginate={"per_page": 20}).configure(FixedCostsTab(getItems))
    if request.method == 'POST':
        # form1 = FixedCostsForm(request.POST)
        # name = form1['name'].value()
        # date = form1['date'].value()
        # quantity = form1['quantity'].value()
        # value = form1['value'].value()

        form = DayForm(request.POST)
        min_date = form['min_date_field'].value()
        max_date = form['max_date_field'].value()
        getItems = FixedCostsRepository().getAll(min_date, max_date)
        form = MonthForm(request.POST)
        table = RequestConfig(request, paginate={"per_page": 20}).configure(FixedCostsTab(getItems))
        return render(request, 'fixedcosts.html', {"table": table, 'form': form, 'form1': form1})
    return render(request, 'fixedcosts.html', {"table": table, 'form': form, 'form1': form1})