from django.db.models import Avg, Func

from reportsapp.database_repository.bestproducts import Round
from reportsapp.database_repository.models import Costs


class CostsRepository():
    select_data = {"date_cost": "DATE_FORMAT( date_cost,'%%Y-%%m-%%d')"}

    def createAll(self,invoice_no, cost_name, date_cost, num_items_buy, unit_price_usd, complete_net_total_usd,
                                        complete_total_buy_usd, complete_tax_total_usd, complete_shipping_total_usd,
                                        complete_shipping_per_unit_usd, complete_unit_cost_usd, complete_unit_price_pln,
                                        complete_total_buy_pln, complete_shipping_per_unit_pln,
                                        complete_shipping_total_pln,
                                        complete_tax_total_pln, complete_unit_cost_pln, complete_net_total_pln,
                                        complete_net_total_cost_pln, complete_net_total_cost_usd):
        self.data = Costs.objects.create(invoice_no=invoice_no,cost_name=cost_name, date_cost=date_cost, num_items_buy=num_items_buy,
                                         unit_price_usd=unit_price_usd, tax_total_usd=complete_tax_total_usd,
                                         shipping_total_usd=complete_shipping_total_usd,
                                         net_total_usd=complete_net_total_usd, total_buy_usd=complete_total_buy_usd,
                                         shipping_per_unit_usd=complete_shipping_per_unit_usd, unit_price=complete_unit_price_pln,
                                         tax_total=complete_tax_total_pln, shipping_total=complete_shipping_total_pln, net_total=complete_net_total_pln,
                                         total_buy=complete_total_buy_pln, shipping_per_unit=complete_shipping_per_unit_pln,
                                         unit_cost_pln=complete_unit_cost_pln,unit_cost=complete_unit_cost_usd,net_cost_usd=complete_net_total_cost_usd,net_cost_pln=complete_net_total_cost_pln)
        return self.data

    def getAll(self,min_date, max_date):
        self.data = Costs.objects.extra(select=self.select_data).filter(date_cost__range=(min_date, max_date) ).order_by('-date_cost')
        return self.data

    def getAllPlot(self):
        self.data = Costs.objects.values_list('cost_name', 'date_cost', 'num_items_buy', 'unit_price_usd',
                                              'tax_total_usd',
                                              'shipping_total_usd', 'shipping_per_unit_usd', 'net_total_usd',
                                              'total_buy_usd', 'unit_cost', 'unit_cost_pln')
        return self.data

    def getAllPlotPLN(self):
        self.data = Costs.objects.values_list('cost_name', 'date_cost', 'num_items_buy', 'unit_price',
                                              'tax_total',
                                              'shipping_total', 'shipping_per_unit', 'net_total',
                                              'total_buy', 'unit_cost').aggregate(Round(
            Avg('unit_price', 'tax_total', 'shipping_total', 'shipping_per_unit', 'net_total', 'total_buy', 'unit_cost',
                'unit_cost_pln'), 2))
        return self.data
