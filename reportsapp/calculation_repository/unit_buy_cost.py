

class UnitCostCalculationPLN():
    def calc(self,unit_price_usd, complete_shipping_per_unit_pln,num_items_buy, complete_tax_total_pln):
        self.value = self.value = float(unit_price_usd) + float(complete_shipping_per_unit_pln) + float(complete_tax_total_pln / int(num_items_buy))

        return self.value