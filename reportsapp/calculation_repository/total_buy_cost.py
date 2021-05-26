class TotalBuyUSD:

    def calc(self, complete_net_total_cost_usd):
        self.value = complete_net_total_cost_usd  * 1.23
        return self.value


class TotalBuyPLN():

    def calc(self, complete_net_total_cost_pln):
        self.value = complete_net_total_cost_pln * 1.23
        return self.value
