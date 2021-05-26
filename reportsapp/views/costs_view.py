from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django_tables2 import RequestConfig
from django_tables2.export import TableExport
from datetime import datetime
from reportsapp.calculation_repository.Tax_Percent_change import TaxPercentChangeUSD, TaxPercentChangePLN
from reportsapp.calculation_repository.net_cost_total import NetCostTotalCalculation, NetCostTotalCalculationPLN
from reportsapp.calculation_repository.net_total import NetTotalCalculation
from reportsapp.calculation_repository.pln_usd_change import CurrencyExchangePLNtoUSD
from reportsapp.calculation_repository.shipping import ShippingCalculation, ShippingCalculationPLN
from reportsapp.calculation_repository.shipping_unit_cost import ShippingPerUnitCalculation, \
    ShippingPerUnitCalculationPLN
from reportsapp.calculation_repository.total_buy_cost import TotalBuyUSD, TotalBuyPLN
from reportsapp.calculation_repository.unit_buy_cost import UnitCostCalculationPLN
from reportsapp.calculation_repository.unit_buy_cost_usd import UnitCostCalculationUSD
from reportsapp.calculation_repository.usd_pln_change import CurrencyExchangeUSDtoPLN
from reportsapp.dash_plotly_repository.costs_plotly_dashboard import createPlotCosts
from reportsapp.database_repository.costs import CostsRepository
from reportsapp.database_repository.currency import CurrencyRepository
from reportsapp.database_repository.models import Documents
from reportsapp.database_repository.products import ProductsRepository
from reportsapp.doc_storage.document_validator import validateDocumentExtension
from reportsapp.doc_storage.handle_uploaded_file import handleUploadedFile, handleUploadedFilePLN
from reportsapp.forms import CostsForm, CurrencyForm, StartPartneredDeliveryForm, DayForm, DocumentForm
from reportsapp.tabels_repository.tabels import CostsTab, CostsTabPLN


@require_http_methods(["GET", "POST"])
def costs_post(request):
    global uploaded_file_url
    now = datetime.now()
    datenow = now.strftime("%Y-%m-%d")
    form_day = DayForm()
    form = CostsForm()
    form_select = CurrencyForm()
    getItems = CostsRepository().getAll(min_date='2019-01-01', max_date='2050-01-01')
    rows_products = ProductsRepository().getAll()
    listbox = StartPartneredDeliveryForm(rows_products)
    table = RequestConfig(request, paginate={"per_page": 10}).configure(CostsTab(getItems))
    tablePLN = RequestConfig(request, paginate={"per_page": 10}).configure(CostsTabPLN(getItems))
    rows = CostsRepository().getAllPlot()
    plot_bar_Wide = createPlotCosts(rows)
    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        table = tablePLN
        exporter = TableExport(export_format, table, exclude_columns=('Delete'))
        return exporter.response('Drony_raporty_koszty_export ' + datenow + '.{}'.format(export_format))
    if request.method == 'POST':
        form = CostsForm(request.POST)
        form_select = CurrencyForm(request.POST)
        form_day = DayForm(request.POST)
        min_date = form_day['min_date_field'].value()
        max_date = form_day['max_date_field'].value()
        file = DocumentForm(request.POST, request.FILES)
        if file['myfile'].value() is not None:
            file = request.FILES['myfile']
            validateDocumentExtension(file)
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            uploaded_file_url = fs.url(filename)
            instance = Documents(document=uploaded_file_url)
            instance.save()
        if form_select['select'].value() is None:
            getItems = CostsRepository().getAll(min_date, max_date)
            table = RequestConfig(request, paginate={"per_page": 50}).configure(CostsTab(getItems))
            tablePLN = RequestConfig(request, paginate={"per_page": 50}).configure(CostsTabPLN(getItems))
            return render(request, 'costs.html',
                          {'DocumentForm': DocumentForm, 'cost_form': CostsForm, 'form_select': form_select,
                           "table": table, "tablePLN": tablePLN,
                           'form_day': form_day,
                           "plot": plot_bar_Wide, "listbox": listbox})

        elif form_select['select'].value() == "USD" and file is not None:
            handleUploadedFile(uploaded_file_url)
            return redirect('/costs/')

        elif form_select['select'].value() == "USD" and file is None:
            listbox = request.POST['browser']
            cost_name = listbox
            invoice_no = form['invoice_no'].value()
            date_cost = form['date_cost'].value()
            num_items_buy = form['num_items_buy'].value()
            unit_price_usd = form['unit_price_usd'].value()
            tax_total_usd = form['tax_total_usd'].value()
            shipping_total_usd = form['shipping_total_usd'].value()
            net_total = form['net_total_usd'].value()

            avegare_exchange_rate = CurrencyRepository().getAll(date_cost)
            complete_net_total_usd = NetTotalCalculation().calc(num_items_buy, unit_price_usd)
            complete_tax_total_usd = TaxPercentChangeUSD().taxTotal(complete_net_total_usd, tax_total_usd)
            complete_shipping_total_usd = ShippingCalculation().calc(net_total, shipping_total_usd,
                                                                     complete_net_total_usd)
            complete_shipping_per_unit_usd = ShippingPerUnitCalculation().calc(complete_shipping_total_usd,
                                                                               num_items_buy)
            complete_unit_cost_usd = UnitCostCalculationUSD().calc(unit_price_usd, complete_shipping_per_unit_usd,
                                                                   num_items_buy, complete_tax_total_usd)
            complete_net_total_cost_usd = NetCostTotalCalculation().calc(complete_unit_cost_usd, num_items_buy)
            complete_total_buy_usd = TotalBuyUSD().calc(complete_net_total_cost_usd)
            complete_unit_price_pln = CurrencyExchangeUSDtoPLN().unitPriceExchange(unit_price_usd,
                                                                                   avegare_exchange_rate)
            complete_total_buy_pln = CurrencyExchangeUSDtoPLN().totalBuyExchange(complete_total_buy_usd,
                                                                                 avegare_exchange_rate)
            complete_shipping_per_unit_pln = CurrencyExchangeUSDtoPLN().shippingPerUnitExchange(
                complete_shipping_per_unit_usd, avegare_exchange_rate)
            complete_shipping_total_pln = CurrencyExchangeUSDtoPLN().schippingExchange(complete_shipping_total_usd,
                                                                                       avegare_exchange_rate)
            complete_tax_total_pln = CurrencyExchangeUSDtoPLN().taxTotalExchange(complete_tax_total_usd,
                                                                                 avegare_exchange_rate)
            complete_unit_cost_pln = CurrencyExchangeUSDtoPLN().unitCostExchange(complete_unit_cost_usd,
                                                                                 avegare_exchange_rate)
            complete_net_total_pln = CurrencyExchangeUSDtoPLN().netTotalExchange(complete_net_total_usd,
                                                                                 avegare_exchange_rate)
            complete_net_total_cost_pln = CurrencyExchangeUSDtoPLN().netTotalCostExchange(complete_net_total_cost_usd,
                                                                                          avegare_exchange_rate)

            CostsRepository().createAll(invoice_no, cost_name, date_cost, num_items_buy, unit_price_usd,
                                        complete_net_total_usd,
                                        complete_total_buy_usd, complete_tax_total_usd, complete_shipping_total_usd,
                                        complete_shipping_per_unit_usd, complete_unit_cost_usd, complete_unit_price_pln,
                                        complete_total_buy_pln, complete_shipping_per_unit_pln,
                                        complete_shipping_total_pln,
                                        complete_tax_total_pln, complete_unit_cost_pln, complete_net_total_pln,
                                        complete_net_total_cost_pln, complete_net_total_cost_usd)
            return redirect('/costs/')

        elif form_select['select'].value() == "PLN" and file is not None:
            handleUploadedFilePLN(uploaded_file_url)
            return redirect('/costs/')

        elif form_select['select'].value() == "PLN" and file is None:
            listbox = request.POST['browser']
            invoice_no = form['invoice_no'].value()
            cost_name = listbox
            date_cost = form['date_cost'].value()
            num_items_buy = form['num_items_buy'].value()
            unit_price_usd = form['unit_price_usd'].value()
            tax_total_usd = form['tax_total_usd'].value()
            shipping_total_usd = form['shipping_total_usd'].value()
            net_total = form['net_total_usd'].value()
            avegare_exchange_rate = CurrencyRepository().getAll(date_cost)
            complete_net_total_pln = NetTotalCalculation().calc(num_items_buy, unit_price_usd)
            complete_tax_total_pln = TaxPercentChangePLN().taxTotal(tax_total_usd, complete_net_total_pln)
            complete_shipping_total_pln = ShippingCalculationPLN().calc(net_total, shipping_total_usd,
                                                                        complete_net_total_pln)
            complete_shipping_per_unit_pln = ShippingPerUnitCalculationPLN().calc(complete_shipping_total_pln,
                                                                                  num_items_buy)
            complete_unit_cost_pln = UnitCostCalculationPLN().calc(unit_price_usd, complete_shipping_per_unit_pln,
                                                                   num_items_buy, complete_tax_total_pln)
            complete_net_total_cost_pln = NetCostTotalCalculationPLN().calc(complete_unit_cost_pln, num_items_buy)
            complete_total_buy_pln = TotalBuyPLN().calc(complete_net_total_cost_pln)
            complete_unit_price_pln = unit_price_usd
            complete_unit_price_usd = CurrencyExchangePLNtoUSD().unitPriceExchange(unit_price_usd,
                                                                                   avegare_exchange_rate)
            complete_tax_total_usd = CurrencyExchangePLNtoUSD().taxTotalExchange(complete_tax_total_pln,
                                                                                 avegare_exchange_rate)
            complete_shipping_total_usd = CurrencyExchangePLNtoUSD().ShippingTotalExchange(complete_shipping_total_pln,
                                                                                           avegare_exchange_rate)
            complete_total_buy_usd = CurrencyExchangePLNtoUSD().totalBuyExchange(complete_total_buy_pln,
                                                                                 avegare_exchange_rate)
            complete_shipping_per_unit_usd = CurrencyExchangePLNtoUSD().shippingPerUnitExchange(
                complete_shipping_per_unit_pln,
                avegare_exchange_rate)
            complete_net_total_usd = CurrencyExchangePLNtoUSD().netTotalExchange(complete_net_total_pln,
                                                                                 avegare_exchange_rate)
            complete_net_total_cost_usd = CurrencyExchangePLNtoUSD().netTotalCostExchange(complete_net_total_cost_pln,
                                                                                          avegare_exchange_rate)
            complete_unit_cost_usd = CurrencyExchangePLNtoUSD().unitCostExchange(complete_unit_cost_pln,
                                                                                 avegare_exchange_rate)

            CostsRepository().createAll(invoice_no, cost_name, date_cost, num_items_buy, unit_price_usd, complete_net_total_usd,
                                        complete_total_buy_usd, complete_tax_total_usd, complete_shipping_total_usd,
                                        complete_shipping_per_unit_usd, complete_unit_cost_usd, complete_unit_price_pln,
                                        complete_total_buy_pln, complete_shipping_per_unit_pln,
                                        complete_shipping_total_pln,
                                        complete_tax_total_pln, complete_unit_cost_pln, complete_net_total_pln,
                                        complete_net_total_cost_pln, complete_net_total_cost_usd)
            return redirect('/costs/')

    return render(request, 'costs.html',
                  {'DocumentForm': DocumentForm, 'cost_form': CostsForm, 'form_select': form_select, "table": table,
                   "tablePLN": tablePLN, 'form_day': form_day,
                   "plot": plot_bar_Wide, "listbox": listbox})
