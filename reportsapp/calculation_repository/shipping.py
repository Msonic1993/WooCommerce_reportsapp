from reportsapp.calculation_repository.net_total import NetTotalCalculation


class ShippingCalculation():

    def calc(self,net_total,shipping_total_usd,complete_net_total_usd):
        self.coefficient =   (float(net_total) + float(shipping_total_usd)) / float(net_total)
        self.net_and_shipping =float(complete_net_total_usd) * self.coefficient
        self.value = self.net_and_shipping - float(complete_net_total_usd)

        return self.value

class ShippingCalculationPLN():

    def calc(self, net_total, shipping_total_usd, complete_net_total_pln):
        self.coefficient = (float(net_total) + float(shipping_total_usd)) / float(net_total)
        self.net_and_shipping = float(complete_net_total_pln) * self.coefficient
        self.value = self.net_and_shipping - float(complete_net_total_pln)

        return self.value