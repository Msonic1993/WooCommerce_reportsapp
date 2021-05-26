from django.db.models import Func
from reportsapp.database_repository.database import baseLocal


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 2)'


class IncomeVsExpensesRepository():
    def getAll(self, min_date, max_date):
        select_data = {"date": "DATE_FORMAT( date_cost,'%%Y-%%m')"}
        # self.data = Costs.objects.filter(date_cost__range=[min_date ,max_date ]).extra(select=select_data).values('date').annotate(
        #     count_items=Sum('num_items_buy'), count_net_value=Round(Sum('net_total')), count_tax=Round(Sum('tax_total')),
        #     count_total_buy=Round(Sum('total_buy'))).values('date', 'count_items', 'count_net_value',
        #                                                  'count_tax', 'count_total_buy').order_by('-date')
        DronyWPDB = baseLocal()
        self.data = 'SELECT DATE_FORMAT(o.date_created,"%Y-%m") AS `date`,' \
                    'ROUND(SUM(o.product_net_revenue),2) AS `count_net_value`, ' \
                    'COALESCE(ROUND(x.net_cost_pln ,2),0) AS net_cost_pln, ' \
                    'ROUND(sum(o.product_net_revenue),2)-COALESCE(ROUND(x.net_cost_pln,2),0) AS wynik ' \
                    'FROM wp_wc_order_product_lookup AS  o ' \
                    'JOIN wp_wc_order_stats p ON p.order_id = o.order_id ' \
                    'LEFT JOIN (SELECT DATE_FORMAT(c.date_cost, "%Y-%m") AS _date, SUM(c.net_cost_pln) AS net_cost_pln FROM reportsapp_costs AS c GROUP BY   _date) AS x ' \
                    'ON DATE_FORMAT(o.date_created, "%Y-%m") = x._date ' \
                    'WHERE DATE_FORMAT(o.date_created,"%Y-%m") BETWEEN "'+min_date+'" AND "'+max_date+'" AND p.`status` IN ("wc-completed","wc-problem","wc-on-hold","wc-wyslane","wc-refunded","wc-processing") ' \
                     'GROUP BY DATE_FORMAT(o.date_created,"%Y-%m") order by DATE_FORMAT(o.date_created,"%Y-%m") DESC'

        DBcursor = DronyWPDB.cursor(dictionary=True)
        DBcursor.execute(self.data)
        rows = DBcursor.fetchall()
        products_list = rows
        return products_list

    def getAllmargin(self):
        select_data = {"date": "DATE_FORMAT( date_cost,'%%Y-%%m')"}
        DronyWPDB = baseLocal()
        self.data = 'SELECT DATE_FORMAT(c.date_cost, "%Y-%m-%d") as date,' \
                    ' c.cost_name as name,' \
                    ' ROUND(IFNULL(c.unit_cost_pln, 0),2) AS unit_cost,' \
                    ' ROUND((s.Unit_price / "1.23"),2) as net_price,' \
                    ' ROUND((s.Unit_price / "1.23"),2)- ROUND(IFNULL(c.unit_cost_pln, 0),2) AS value_margin, ' \
                    'CONCAT(ROUND((ROUND((s.Unit_price / "1.23"),2)- ROUND(IFNULL(c.unit_cost_pln, 0),2)) / ROUND((s.Unit_price / "1.23"),2)*"100",0),"%") AS percent_margin' \
                    ' FROM reportsapp_costs AS c ' \
                    'LEFT JOIN reportsapp_historical_warehouse s ON  s.product_name = c.cost_name ' \
                    'GROUP BY c.cost_name'

        DBcursor = DronyWPDB.cursor(dictionary=True)
        DBcursor.execute(self.data)
        rows = DBcursor.fetchall()
        products_list = rows
        return products_list
