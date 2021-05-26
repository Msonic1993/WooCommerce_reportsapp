from reportsapp.calculation_repository.net_total import NetTotalCalculation


class TaxPercentChangeUSD:


    def taxTotal(self, complete_net_total_usd,tax_total_usd):
        self.value = (complete_net_total_usd * float(tax_total_usd) / 100) * 1.032
        return self.value

class TaxPercentChangePLN():

    def taxTotal(self, tax_total_usd, complete_net_total_pln):
        self.value = (complete_net_total_pln * float(tax_total_usd) / 100) * 1.032
        return self.value