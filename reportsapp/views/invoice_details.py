from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django_tables2 import RequestConfig
from django_tables2.export import TableExport
from datetime import datetime
from reportsapp.dash_plotly_repository.costs_plotly_dashboard import createPlotCosts
from reportsapp.database_repository.costs import CostsRepository
from reportsapp.database_repository.invoice import InvoiceRepository
from reportsapp.database_repository.products import ProductsRepository
from reportsapp.forms import CostsForm, CurrencyForm, StartPartneredDeliveryForm, DayForm, DocumentForm
from reportsapp.tabels_repository.tabels import CostsTab, CostsTabPLN


@require_http_methods(["GET", "POST"])
def invoiceDetails(request, invoice_no):
    global uploaded_file_url
    now = datetime.now()  # current date and time
    datenow = now.strftime("%Y-%m-%d")
    form_day = DayForm()
    form = CostsForm()
    form_select = CurrencyForm()
    getItems = InvoiceRepository().getDetails(min_date='2019-01-01', max_date='2050-01-01', invoice_no=invoice_no)
    rows_products = ProductsRepository().getAll()
    listbox = StartPartneredDeliveryForm(rows_products)
    table = RequestConfig(request, paginate={"per_page": 400}).configure(CostsTab(getItems))
    tablePLN = RequestConfig(request, paginate={"per_page": 400}).configure(CostsTabPLN(getItems))
    rows = CostsRepository().getAllPlot()
    plot_bar_Wide = createPlotCosts(rows)
    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        table = tablePLN
        exporter = TableExport(export_format, table, exclude_columns=('Delete'))
        return exporter.response('Drony_raporty_koszty_export ' + datenow + '.{}'.format(export_format))

    return render(request, 'invoicedetails.html',
                  {'DocumentForm':DocumentForm,'cost_form':CostsForm, 'form_select': form_select, "table": table, "tablePLN": tablePLN, 'form_day': form_day,
                   "plot": plot_bar_Wide, "listbox": listbox})