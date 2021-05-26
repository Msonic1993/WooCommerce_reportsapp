from _csv import reader
from reportsapp.calculation_repository.Tax_Percent_change import TaxPercentChangeUSD, TaxPercentChangePLN
from reportsapp.calculation_repository.net_cost_total import NetCostTotalCalculation, NetCostTotalCalculationPLN
from reportsapp.calculation_repository.net_total import NetTotalCalculation
from reportsapp.calculation_repository.pln_usd_change import CurrencyExchangePLNtoUSD
from reportsapp.calculation_repository.shipping import ShippingCalculation, ShippingCalculationPLN
from reportsapp.calculation_repository.shipping_unit_cost import ShippingPerUnitCalculation, \
    ShippingPerUnitCalculationPLN
from reportsapp.calculation_repository.total_buy_cost import TotalBuyUSD, TotalBuyPLN
from reportsapp.calculation_repository.unit_buy_cost import UnitCostCalculationPLN
from reportsapp.calculation_repository.unit_buy_cost_usd import UnitCostCalculationUSD
from reportsapp.calculation_repository.usd_pln_change import CurrencyExchangeUSDtoPLN
from reportsapp.database_repository.costs import CostsRepository
from reportsapp.database_repository.currency import CurrencyRepository


def handleUploadedFile(uploaded_file_url):
    with open('.'+uploaded_file_url, 'r') as f:
        df = reader(f, delimiter=';')
        next(df, None)
        for row in df:
            invoice_no = row[0]
            cost_name = row[1],
            date_cost = row[2],
            num_items_buy = row[3],
            unit_price_usd = row[4],
            tax_total_usd = row[5],
            shipping_total_usd = row[6],
            net_total = row[7]
            avegare_exchange_rate = CurrencyRepository().getAll(date_cost)
            complete_net_total_usd = NetTotalCalculation().calc("".join(num_items_buy), "".join(unit_price_usd))
            complete_tax_total_usd = TaxPercentChangeUSD().taxTotal(complete_net_total_usd, "".join(tax_total_usd))
            complete_shipping_total_usd = ShippingCalculation().calc("".join(net_total), "".join(shipping_total_usd),
                                                                     complete_net_total_usd)
            complete_shipping_per_unit_usd = ShippingPerUnitCalculation().calc(complete_shipping_total_usd,
                                                                               "".join(num_items_buy))
            complete_unit_cost_usd = UnitCostCalculationUSD().calc("".join(unit_price_usd), complete_shipping_per_unit_usd,
                                                                   "".join(num_items_buy), complete_tax_total_usd)
            complete_net_total_cost_usd = NetCostTotalCalculation().calc(complete_unit_cost_usd, "".join(num_items_buy))
            complete_total_buy_usd = TotalBuyUSD().calc(complete_net_total_cost_usd)
            complete_unit_price_pln = CurrencyExchangeUSDtoPLN().unitPriceExchange("".join(unit_price_usd),
                                                                                   avegare_exchange_rate)
            complete_total_buy_pln = CurrencyExchangeUSDtoPLN().totalBuyExchange(complete_total_buy_usd,
                                                                                 avegare_exchange_rate)
            complete_shipping_per_unit_pln = CurrencyExchangeUSDtoPLN().shippingPerUnitExchange(
                complete_shipping_per_unit_usd, avegare_exchange_rate)
            complete_shipping_total_pln = CurrencyExchangeUSDtoPLN().schippingExchange(complete_shipping_total_usd,
                                                                                       avegare_exchange_rate)
            complete_tax_total_pln = CurrencyExchangeUSDtoPLN().taxTotalExchange(complete_tax_total_usd,
                                                                                 avegare_exchange_rate)
            complete_unit_cost_pln = CurrencyExchangeUSDtoPLN().unitCostExchange(complete_unit_cost_usd,
                                                                                 avegare_exchange_rate)
            complete_net_total_pln = CurrencyExchangeUSDtoPLN().netTotalExchange(complete_net_total_usd,
                                                                                 avegare_exchange_rate)
            complete_net_total_cost_pln = CurrencyExchangeUSDtoPLN().netTotalCostExchange(complete_net_total_cost_usd,
                                                                                          avegare_exchange_rate)

            CostsRepository().createAll(invoice_no, "".join(cost_name), "".join(date_cost), "".join(num_items_buy), "".join(unit_price_usd),
                                        complete_net_total_usd, complete_tax_total_usd, complete_shipping_total_usd,
                                        complete_shipping_per_unit_usd, complete_unit_cost_usd,
                                        complete_net_total_cost_usd,
                                        complete_total_buy_usd, complete_unit_price_pln, complete_total_buy_pln,
                                        complete_shipping_per_unit_pln, complete_shipping_total_pln,
                                        complete_tax_total_pln,
                                        complete_unit_cost_pln, complete_net_total_pln, complete_net_total_cost_pln)

    return "Plik zaimportowany"



def handleUploadedFilePLN(uploaded_file_url):
    with open('.'+uploaded_file_url, 'r') as f:
        df = reader(f, delimiter=';')
        next(df, None)
        for row in df:
            invoice_no = row[0]
            cost_name = row[1],
            date_cost = row[2],
            num_items_buy = row[3],
            unit_price_usd = row[4],
            tax_total_usd = row[5],
            shipping_total_usd = row[6],
            net_total = row[7]
            avegare_exchange_rate = CurrencyRepository().getAll(date_cost)
            complete_net_total_pln = NetTotalCalculation().calc("".join(num_items_buy), "".join(unit_price_usd))
            complete_tax_total_pln = TaxPercentChangePLN().taxTotal("".join(tax_total_usd), complete_net_total_pln)
            complete_shipping_total_pln = ShippingCalculationPLN().calc("".join(net_total), "".join(shipping_total_usd),
                                                                        complete_net_total_pln)
            complete_shipping_per_unit_pln = ShippingPerUnitCalculationPLN().calc(complete_shipping_total_pln,
                                                                                  "".join(num_items_buy))
            complete_unit_cost_pln = UnitCostCalculationPLN().calc("".join(unit_price_usd), complete_shipping_per_unit_pln,
                                                                   "".join(num_items_buy), complete_tax_total_pln)
            complete_net_total_cost_pln = NetCostTotalCalculationPLN().calc(complete_unit_cost_pln, "".join(num_items_buy))
            complete_total_buy_pln = TotalBuyPLN().calc(complete_net_total_cost_pln)
            complete_unit_price_pln = "".join(unit_price_usd)
            complete_unit_price_usd = CurrencyExchangePLNtoUSD().unitPriceExchange("".join(unit_price_usd),
                                                                                   avegare_exchange_rate)
            complete_tax_total_usd = CurrencyExchangePLNtoUSD().taxTotalExchange(complete_tax_total_pln,
                                                                                 avegare_exchange_rate)
            complete_shipping_total_usd = CurrencyExchangePLNtoUSD().ShippingTotalExchange(complete_shipping_total_pln,
                                                                                           avegare_exchange_rate)
            complete_total_buy_usd = CurrencyExchangePLNtoUSD().totalBuyExchange(complete_total_buy_pln,
                                                                                 avegare_exchange_rate)
            complete_shipping_per_unit_usd = CurrencyExchangePLNtoUSD().shippingPerUnitExchange(
                complete_shipping_per_unit_pln, avegare_exchange_rate)
            complete_net_total_usd = CurrencyExchangePLNtoUSD().netTotalExchange(complete_net_total_pln,
                                                                                 avegare_exchange_rate)
            complete_net_total_cost_usd = CurrencyExchangePLNtoUSD().netTotalCostExchange(complete_net_total_cost_pln,
                                                                                          avegare_exchange_rate)
            complete_unit_cost_usd = CurrencyExchangePLNtoUSD().unitCostExchange(complete_unit_cost_pln,
                                                                                 avegare_exchange_rate)

            CostsRepository().createAll(invoice_no, "".join(cost_name), "".join(date_cost), "".join(num_items_buy), "".join(unit_price_usd),
                                        complete_net_total_usd,
                                        complete_total_buy_usd, complete_tax_total_usd, complete_shipping_total_usd,
                                        complete_shipping_per_unit_usd, complete_unit_cost_usd, complete_unit_price_pln,
                                        complete_total_buy_pln, complete_shipping_per_unit_pln,
                                        complete_shipping_total_pln,
                                        complete_tax_total_pln, complete_unit_cost_pln, complete_net_total_pln,
                                        complete_net_total_cost_pln, complete_net_total_cost_usd)
    return "Plik zaimportowany"