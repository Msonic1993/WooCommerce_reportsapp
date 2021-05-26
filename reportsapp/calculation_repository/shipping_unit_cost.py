from reportsapp.calculation_repository.shipping import ShippingCalculation


class ShippingPerUnitCalculation():
    def calc(self,complete_shipping_total_usd,num_items_buy):
        self.value = float(complete_shipping_total_usd) / float(num_items_buy)

        return self.value


class ShippingPerUnitCalculationPLN():
    def calc(self,complete_shipping_total_pln,num_items_buy):
        self.value = float(complete_shipping_total_pln) / float(num_items_buy)

        return self.value
