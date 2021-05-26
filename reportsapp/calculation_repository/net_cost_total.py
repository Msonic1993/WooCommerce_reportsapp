class NetCostTotalCalculation():
    def calc(self,complete_unit_cost_usd,num_items_buy):
        self.value = float(complete_unit_cost_usd) * int(num_items_buy)
        return self.value



class NetCostTotalCalculationPLN():
    def calc(self,complete_unit_cost_pln,num_items_buy):
        self.value = float(complete_unit_cost_pln) * int(num_items_buy)
        return self.value