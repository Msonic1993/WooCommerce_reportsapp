from datetime import datetime
from django.shortcuts import render
from django_tables2 import RequestConfig
from reportsapp.database_repository.invoice import InvoiceRepository
from reportsapp.forms import DayForm
from reportsapp.tabels_repository.tabels import InvoiceTab


def invoiceList(request):
    now = datetime.now()
    form_day = DayForm()
    getItems = InvoiceRepository().getAll()
    table = RequestConfig(request, paginate={"per_page": 500}).configure(InvoiceTab(getItems))

    return render(request, 'invoice.html',
                  {'table': table,'form_day':form_day})


