import django_tables2 as tables
from django_tables2 import A, Table


from reportsapp.database_repository.models import WpWcOrderStats, Costs


class NumberColumn(tables.Column):
    def render(self, value):
        return '{:0.2f}'.format(value)


class OrdersTab(tables.Table):
    date = tables.Column(verbose_name='Data zamówienia', footer="Total:")

    count_items = tables.Column(verbose_name='Ilość produktów',
                                footer=lambda table: sum(x["count_items"] for x in table.data)
                                )
    count_orders = tables.Column(verbose_name='Ilość zamówień',
                                 footer=lambda table: sum(x["count_orders"] for x in table.data)
                                 )
    count_net_value = tables.Column(verbose_name='Wartość netto',
                                    footer=lambda table: round(sum(x["count_net_value"] for x in table.data), 2))
    count_tax = tables.Column(verbose_name='Wartość VAT',
                              footer=lambda table: round(sum(x["count_tax"] for x in table.data), 2))
    count_coupons = tables.Column(verbose_name='Wartość rabatów',
                              footer=lambda table: round(sum(x["count_coupons"] for x in table.data), 2))
    count_total_sales = tables.Column(verbose_name='Wartość brutto',
                                      footer=lambda table: round(sum(x["count_total_sales"] for x in table.data), 2))

    class Meta:
        model = WpWcOrderStats
        fields = ('date', 'count_orders', 'count_items', 'count_net_value', 'count_tax', 'count_coupons','count_total_sales' )
        attrs = {"class": "styled-table"}


class OrdersMonthTab(tables.Table):
    date = tables.Column(verbose_name='Miesiąc', footer="Total:")

    count_items = tables.Column(verbose_name='Ilość zamówień',
                                footer=lambda table: sum(x["count_items"] for x in table.data)
                                )
    count_net_value = NumberColumn(verbose_name='Wartość netto',
                                    footer=lambda table: sum(x["count_net_value"] for x in table.data))
    count_tax = NumberColumn(verbose_name='Wartość VAT', footer=lambda table: sum(x["count_tax"] for x in table.data))
    count_total_sales = NumberColumn(verbose_name='Wartość brutto',
                                      footer=lambda table: sum(x["count_total_sales"] for x in table.data))

    class Meta:
        model = WpWcOrderStats
        fields = ('date', 'count_items', 'count_net_value', 'count_tax', 'count_total_sales')
        attrs = {"class": "styled-table"}

class InvoiceTab(tables.Table):
    date_cost = tables.Column(verbose_name='Data na fakturze  ')
    invoice_no = tables.Column(verbose_name='Nr faktury')
    total_buy = tables.Column(verbose_name='Total brutto z faktury')
    details = tables.LinkColumn('invoiceDetails', text='Szczegóły', args=[A('invoice_no')], attrs={
        'a': {'class': 'btn btn-info'} })
    class Meta:
        model = Costs
        fields = ('invoice_no', 'date_cost', 'total_buy', 'details')
        attrs = {"class": "styled-table", "id": "costs"}



class CostsTab(tables.Table):
    invoice_no = tables.Column(verbose_name='Nr faktury',
                              footer="Total:"
                              )
    cost_name = tables.Column(verbose_name='Nazwa towaru',
                              footer="Total:"
                              )
    date_cost = tables.Column(verbose_name='Data na fakturze  ', footer="Total:")
    num_items_buy = tables.Column(verbose_name='Ilość',
                                  )
    unit_price_usd = NumberColumn(verbose_name='Cena za sztukę [USD]', footer="Total:")
    tax_total_usd = NumberColumn(verbose_name='Koszt cła [USD]')
    shipping_total_usd = NumberColumn(verbose_name='Koszt transportu [USD]',
                                      footer="Total:")
    shipping_per_unit_usd = NumberColumn(verbose_name='Koszt transportu 1 sztuki [USD]',
                                         footer="Total:")
    unit_cost = NumberColumn(verbose_name='Koszt zakupu sztuki [USD]')
    net_total_usd = NumberColumn(verbose_name='Wartość Netto [USD]',
                                 footer="Total:")
    total_buy_usd = NumberColumn(verbose_name='Wartość brutto [USD]',
                                 )
    net_cost_usd = NumberColumn(verbose_name='Koszt netto [USD]',
                                 )

    delete = tables.LinkColumn('detail', text='Usuń ten koszt', args=[A('id')], attrs={
        'a': {'class': 'btn btn-danger'}
    })

    class Meta:
        model = Costs
        fields = ('invoice_no','cost_name', 'date_cost', 'num_items_buy', 'unit_price_usd','net_total_usd', 'tax_total_usd', 'shipping_total_usd',
                  'shipping_per_unit_usd','unit_cost', 'net_cost_usd', 'total_buy_usd', 'delete')
        attrs = {"class": "styled-table", "id": "costs"}


class CostsTabPLN(tables.Table):
    cost_name = tables.Column(verbose_name='Nazwa', footer="Total:")
    invoice_no = tables.Column(verbose_name='Nr faktury')
    date_cost = tables.Column(verbose_name='Data na fakturze  ')
    num_items_buy = tables.Column(verbose_name='Ilość',footer=lambda table: round(sum(x.num_items_buy for x in table.data),2))
    unit_price = NumberColumn(verbose_name='Cena za sztukę [PLN]')
    tax_total = NumberColumn(verbose_name='Kosz cła [PLN]', footer=lambda table: round(sum(x.tax_total for x in table.data),2))
    shipping_total = NumberColumn(verbose_name='Koszt transportu [PLN]', footer=lambda table: round(sum(x.shipping_total for x in table.data),2))
    shipping_per_unit = NumberColumn(verbose_name='Koszt transportu 1 sztuki [PLN]')
    net_total = NumberColumn(verbose_name='Wartość Netto [PLN]', footer=lambda table: round(sum(x.net_total for x in table.data),2))
    total_buy = NumberColumn(verbose_name='Koszt brutto [PLN]',footer=lambda table: round(sum(x.total_buy for x in table.data),2))
    unit_cost_pln = NumberColumn(verbose_name='Koszt zakupu sztuki [PLN]')
    net_cost_pln = NumberColumn(verbose_name='Koszt netto [PLN]',footer=lambda table: round(sum(x.net_cost_pln for x in table.data),2)
                                )
    delete = tables.LinkColumn('detail', text='Usuń ten koszt', args=[A('id')], attrs={
        'a': {'class': 'btn btn-danger'}
    })

    class Meta:
        model = Costs
        fields = ('invoice_no','cost_name', 'date_cost', 'num_items_buy', 'unit_price','net_total', 'tax_total', 'shipping_total',
                  'shipping_per_unit', 'unit_cost_pln','net_cost_pln', 'total_buy', 'delete')
        attrs = {"class": "styled-table", "id": "costs"}


class IncomeVsExpensesTab(Table):

    date = tables.Column(verbose_name='Miesiąc', footer="Total:")
    count_net_value = NumberColumn(verbose_name='Sprzedaż wartość netto',
                                    footer=lambda table: round(sum(x["count_net_value"] for x in table.data),2))
    net_cost_pln = NumberColumn(verbose_name='Koszty wartość',
                             footer=lambda table: sum(x["net_cost_pln"] for x in table.data))
    wynik = NumberColumn(verbose_name='Wynik wartość', footer=lambda table: round(sum(x["wynik"] for x in table.data),2))

    class Meta:
        sequence = ("date", "count_net_value", "net_cost_pln", "wynik")
        attrs = {"class": "styled-table", "id": "topproduct"}


class MarginValueTab(Table):
    date = tables.Column(verbose_name='Data zakupu towaru', footer="Total:")
    name = tables.Column(verbose_name='Nazwa towaru')
    unit_cost = tables.Column(verbose_name='Koszt zakupu szt. [PLN]')
    net_price = tables.Column(verbose_name='Cena jednostkowa netto [PLN]')
    value_margin = tables.Column(verbose_name='Wartość marży netto [PLN]')
    percent_margin = tables.Column(verbose_name='% marży netto [PLN]')

    class Meta:
        sequence = ("date", "name", "unit_cost", "net_price","value_margin","percent_margin")
        attrs = {"class": "styled-table", "id": "topproduct"}


class BestProductAllTab(Table):
    post_title = tables.Column(verbose_name='Nazwa produktu')
    quantity = tables.Column(verbose_name='Ilość sprzedanych sztuk',
                             footer=lambda table: round(sum(x["quantity"] for x in table.data), 2))
    value = NumberColumn(verbose_name='Wartość sprzedanych sztuk',
                         footer=lambda table: round(sum(x["value"] for x in table.data), 2))
    unit_value = NumberColumn(verbose_name='Wartość sprzedaży sztuki [netto]',
                         footer=lambda table: round(sum(x["unit_value"] for x in table.data), 2))

    class Meta:
        sequence = ("post_title", "quantity", "value", "unit_value")
        attrs = {"class": "styled-table", "id": "topproduct"}


class BestProductTab(Table):
    date = tables.Column(verbose_name='Miesiąc', footer="Total:")
    name = tables.Column(verbose_name='Nazwa produktu')
    quantity = tables.Column(verbose_name='Ilość sprzedanych sztuk',
                             footer=lambda table: round(sum(x["quantity"] for x in table.data), 2))
    value = NumberColumn(verbose_name='Wartość sprzedanych sztuk [netto]',
                         footer=lambda table: round(sum(x["value"] for x in table.data), 2))
    unit_value = NumberColumn(verbose_name='Wartość sprzedaży sztuki [netto]',
                              footer=lambda table: round(sum(x["unit_value"] for x in table.data), 2))

    class Meta:
        sequence = ("date", "name", "quantity", "value", "unit_value")
        attrs = {"class": "styled-table", "id": "topproduct"}


class FixedCostsTab(Table):
    date = tables.Column(verbose_name='Data', footer="Total:")
    name = tables.Column(verbose_name='Nazwa')
    quantity = NumberColumn(verbose_name='Ilość',
                            footer=lambda table: sum(x["quantity"] for x in table.data))
    value = tables.Column(verbose_name='Wartość', footer=lambda table: sum(x["value"] for x in table.data))

    class Meta:
        sequence = ("date", "name", "quantity", "value")
        attrs = {"class": "styled-table", "id": "topproduct"}


class WarehouseTab(Table):
    Name = tables.Column(verbose_name='Nazwa produktu')
    Category = tables.Column(verbose_name='Kategoria produktu')
    Stock = tables.Column(verbose_name='Ilość w magazynie ')
    Price = tables.Column(verbose_name='Cena jednostkowa')
    stan_wartosc = tables.Column(verbose_name='Stan wartość ')

    class Meta:
        sequence = ("Name", "Category", "Stock", "Price", "stan_wartosc")
        attrs = {"class": "styled-table", "id": "topproduct"}



class WarehouseHistoricalTab((tables.Table)):
    product_name = tables.Column(verbose_name='Nazwa produktu')
    product_category = tables.Column(verbose_name='Kategoria produktu')
    quantity = tables.Column(verbose_name='Ilość w magazynie ')
    Unit_price = tables.Column(verbose_name='Cena jednostkowa')
    stock_value = tables.Column(verbose_name='Stan wartość ')
    date= tables.Column(verbose_name='Stan z dnia')

    class Meta:
        sequence = ("date","product_name", "product_category", "quantity", "Unit_price", "stock_value")
        attrs = {"class": "styled-table", "id": "topproduct"}


class GeoOrdersTab(Table):
    city = tables.Column(verbose_name='Miasto')
    ilosc = tables.Column(verbose_name='Ilość zamówień')
    wartość_netto = tables.Column(verbose_name='Total wartość netto')

    class Meta:
        sequence = ("city", "ilosc", "wartość_netto")
        attrs = {"class": "styled-table", "id": "topproduct"}
