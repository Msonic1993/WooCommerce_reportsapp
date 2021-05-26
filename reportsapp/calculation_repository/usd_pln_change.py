from reportsapp.calculation_repository.net_total import NetTotalCalculation
from reportsapp.calculation_repository.shipping import ShippingCalculation


class CurrencyExchangeUSDtoPLN():

    def unitPriceExchange(self, unit_price_usd,avegare_exchange_rate):
        self.value = float(unit_price_usd) * float(avegare_exchange_rate)
        return self.value

    def taxTotalExchange(self, complete_tax_total_usd, avegare_exchange_rate):
        self.value = complete_tax_total_usd * float(avegare_exchange_rate)
        return self.value

    def ShippingTotalExchange(self,shipping_total_usd,num_items_buy,unit_price_usd,avegare_exchange_rate):
        self.value = ShippingCalculation().calc(shipping_total_usd,num_items_buy,unit_price_usd) * float(avegare_exchange_rate)
        return self.value

    def netTotalExchange(self, complete_net_total_usd, avegare_exchange_rate):
        self.value = float(complete_net_total_usd) * float(avegare_exchange_rate)
        return self.value

    def totalBuyExchange(self, complete_total_buy_usd, avegare_exchange_rate):
        self.value = float(complete_total_buy_usd) * float(avegare_exchange_rate)
        return self.value

    def shippingPerUnitExchange(self, complete_shipping_per_unit_usd, avegare_exchange_rate):
        self.value = float(complete_shipping_per_unit_usd) * float(avegare_exchange_rate)
        return self.value

    def unitCostExchange(self,complete_unit_cost_usd,avegare_exchange_rate):
        self.value = float(complete_unit_cost_usd) * float(avegare_exchange_rate)
        return self.value

    def schippingExchange(self, complete_shipping_total_usd, avegare_exchange_rate):
        self.value = float(complete_shipping_total_usd) * float(avegare_exchange_rate)
        return self.value

    def netTotalCostExchange(self, complete_net_total_cost_usd, avegare_exchange_rate):
        self.value = float(complete_net_total_cost_usd) * float(avegare_exchange_rate)
        return self.value