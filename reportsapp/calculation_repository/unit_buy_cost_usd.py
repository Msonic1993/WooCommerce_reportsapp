class UnitCostCalculationUSD():
    def calc(self,unit_price_usd,complete_shipping_per_unit_usd,num_items_buy,complete_tax_total_usd):
        self.value = float(unit_price_usd) + float(complete_shipping_per_unit_usd) + float(complete_tax_total_usd / int(num_items_buy))

        return self.value