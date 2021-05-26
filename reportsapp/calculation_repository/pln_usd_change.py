
class CurrencyExchangePLNtoUSD():

    def unitPriceExchange(self, unit_price_usd, avegare_exchange_rate):
        self.value = float(unit_price_usd) / float(avegare_exchange_rate)
        return self.value

    def taxTotalExchange(self, complete_tax_total_pln, avegare_exchange_rate):
        self.value = float(complete_tax_total_pln) / float(avegare_exchange_rate)
        return self.value

    def ShippingTotalExchange(self, complete_shipping_total_pln, avegare_exchange_rate):
        self.value = float(complete_shipping_total_pln) / float(avegare_exchange_rate)
        return self.value

    def netTotalExchange(self, complete_net_total_usd, avegare_exchange_rate):
        self.value = float(complete_net_total_usd) / float(avegare_exchange_rate)
        return self.value

    def totalBuyExchange(self, complete_total_buy_pln, avegare_exchange_rate):
        self.value = float(complete_total_buy_pln) / float(avegare_exchange_rate)
        return self.value

    def shippingPerUnitExchange(self, complete_shipping_per_unit_pln, avegare_exchange_rate):
        self.value = float(complete_shipping_per_unit_pln) / float(avegare_exchange_rate)
        return self.value

    def unitCostExchange(self, complete_unit_cost_pln, avegare_exchange_rate):
        self.value = float(complete_unit_cost_pln) / float(avegare_exchange_rate)
        return self.value

    def netTotalCostExchange(self, complete_unit_cost_pln, avegare_exchange_rate):
        self.value = float(complete_unit_cost_pln) / float(avegare_exchange_rate)
        return self.value

