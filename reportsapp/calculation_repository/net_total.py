
class NetTotalCalculation():
    def calc(self,num_items_buy,unit_price_usd):
        self.value = int(num_items_buy) * float(unit_price_usd)

        return self.value