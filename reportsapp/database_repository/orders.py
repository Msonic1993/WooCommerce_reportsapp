import json
from datetime import date
from dateutil.relativedelta import relativedelta
from django.db.models import Func
from pandas import DataFrame
from reportsapp.database_repository.models import WpWcOrderStats, WpWcOrderProductLookup
from reportsapp.database_repository.database import baseLocal, baseWP


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 2)'


class OrdersRepository():

    def getAll(self, min_date='2019-01-01', max_date='2050-12-31'):
        DronyWPDB = baseLocal()
        self.data = 'SELECT ' \
                    'DATE_FORMAT(o.date_created,"%Y-%m-%d") AS `date`, ' \
                    'COUNT(DISTINCT o.order_id) AS `count_orders`, ' \
                    'SUM(o.product_qty) AS `count_items`, ' \
                    'ROUND(SUM(o.product_net_revenue),2) AS `count_net_value`, ' \
                    'ROUND(SUM(o.tax_amount),2) AS `count_tax`,  ' \
                    'ROUND(SUM(o.coupon_amount),2) AS `count_coupons`, ' \
                    'Round(SUM(o.product_gross_revenue),2) AS `count_total_sales` ' \
                    'FROM wp_wc_order_product_lookup AS  o  ' \
                    'JOIN wp_wc_order_stats p ON p.order_id = o.order_id ' \
                    'WHERE DATE_FORMAT(o.date_created,"%Y-%m-%d") BETWEEN "'+min_date+'" AND "'+max_date+'" AND p.`status` IN ("wc-completed","wc-problem","wc-on-hold","wc-wyslane","wc-refunded","wc-processing")    '  \
                    ' GROUP BY DATE_FORMAT(o.date_created,"%Y-%m-%d") ORDER BY DATE_FORMAT(o.date_created,"%Y-%m-%d") DESC '

        DBcursor = DronyWPDB.cursor(dictionary=True)
        DBcursor.execute(self.data)
        rows = DBcursor.fetchall()
        products_list = rows
        return products_list

    def getAllmonth(self, min_date, max_date):
        DronyWPDB = baseLocal()
        self.data = 'SELECT ' \
                    'DATE_FORMAT(o.date_created,"%Y-%m") AS `date`, ' \
                    'COUNT(DISTINCT o.order_id) AS `count_orders`, ' \
                    'SUM(o.product_qty) AS `count_items`, ' \
                    'ROUND(SUM(o.product_net_revenue),2) AS `count_net_value`, ' \
                    'ROUND(SUM(o.tax_amount),2) AS `count_tax`,  ' \
                    'ROUND(SUM(o.coupon_amount),2) AS `count_coupons`, ' \
                    'Round(SUM(o.product_gross_revenue),2) AS `count_total_sales` ' \
                    'FROM wp_wc_order_product_lookup AS  o  ' \
                    'JOIN wp_wc_order_stats p ON p.order_id = o.order_id ' \
                    'WHERE DATE_FORMAT(o.date_created,"%Y-%m-%d") BETWEEN "'+min_date+'" AND "'+max_date+'" AND p.`status` IN ("wc-completed","wc-problem","wc-on-hold","wc-wyslane","wc-refunded","wc-processing")     '  \
                    ' GROUP BY DATE_FORMAT(o.date_created,"%Y-%m") ORDER BY DATE_FORMAT(o.date_created,"%Y-%m") DESC'

        DBcursor = DronyWPDB.cursor(dictionary=True)
        DBcursor.execute(self.data)
        rows = DBcursor.fetchall()
        products_list = rows
        print(products_list)
        return products_list






    def getAllquater(self, min_date, max_date):
        DronyWPDB = baseLocal()
        self.data = self.data = 'SELECT ' \
                    'CONCAT(YEAR(o.date_created),"-Q",QUARTER(o.date_created)) AS `date`, ' \
                     'COUNT(DISTINCT o.order_id) AS `count_orders`, ' \
                    'SUM(o.product_qty) AS `count_items`, ' \
                    'ROUND(SUM(o.product_net_revenue),2) AS `count_net_value`, ' \
                    'ROUND(SUM(o.tax_amount),2) AS `count_tax`,  ' \
                    'ROUND(SUM(o.coupon_amount),2) AS `count_coupons`, ' \
                    'Round(SUM(o.product_gross_revenue),2) AS `count_total_sales` ' \
                    'FROM wp_wc_order_product_lookup AS  o  ' \
                    'JOIN wp_wc_order_stats p ON p.order_id = o.order_id ' \
                    'WHERE DATE_FORMAT(o.date_created,"%Y-%m-%d") BETWEEN "'+min_date+'" AND "'+max_date+'" AND p.`status` IN ("wc-completed","wc-problem","wc-on-hold","wc-wyslane","wc-refunded","wc-processing")    '  \
                    'GROUP BY `date` ORDER BY CONCAT(YEAR(o.date_created),"-Q",QUARTER(o.date_created)) DESC'

        DBcursor = DronyWPDB.cursor(dictionary=True)
        DBcursor.execute(self.data)
        rows = DBcursor.fetchall()
        products_list = rows
        return products_list

    def getAllyears(self, min_date, max_date):
        select_data_year = {"date": "YEAR(date_created)"}
        DronyWPDB = baseLocal()
        self.data = self.data = 'SELECT ' \
                                'YEAR(o.date_created) AS `date`, ' \
                                'COUNT(DISTINCT o.order_id) AS `count_orders`, ' \
                    'SUM(o.product_qty) AS `count_items`, ' \
                    'ROUND(SUM(o.product_net_revenue),2) AS `count_net_value`, ' \
                    'ROUND(SUM(o.tax_amount),2) AS `count_tax`,  ' \
                    'ROUND(SUM(o.coupon_amount),2) AS `count_coupons`, ' \
                    'Round(SUM(o.product_gross_revenue),2) AS `count_total_sales` ' \
                    'FROM wp_wc_order_product_lookup AS  o  ' \
                    'JOIN wp_wc_order_stats p ON p.order_id = o.order_id ' \
                    'WHERE DATE_FORMAT(o.date_created,"%Y-%m-%d") BETWEEN "'+min_date+'" AND "'+max_date+'" AND p.`status` IN ("wc-completed","wc-problem","wc-on-hold","wc-wyslane","wc-refunded","wc-processing")    '  \
                                ' GROUP BY `date` ORDER BY `date` DESC'

        DBcursor = DronyWPDB.cursor(dictionary=True)
        DBcursor.execute(self.data)
        rows = DBcursor.fetchall()
        products_list = rows
        return products_list

    def getBarChartDays(self, min_date, max_date):
        DronyWPDB = baseLocal()
        Query = (
                'SELECT  DATE_FORMAT(date_created, "%Y-%m-%d") as "date", SUM(num_items_sold), COUNT(order_id), SUM(net_total), SUM(tax_total), SUM(total_sales) '
                'FROM wp_wc_order_stats '
                ' WHERE DATE_FORMAT(date_created, "%Y-%m-%d") between "' + min_date + '" AND "' + max_date +
                '" AND `status` IN ("wc-completed","wc-problem","wc-on-hold","wc-wyslane","wc-refunded","wc-processing") group by DATE_FORMAT(date_created, "%Y-%m-%d")')

        DBcursor = DronyWPDB.cursor()
        DBcursor.execute(Query)
        rows = DBcursor.fetchall()
        return rows


    def getBarChart(self, min_date, max_date):
        DronyWPDB = baseLocal()
        Query = (
            'SELECT  DATE_FORMAT(date_created, "%Y-%m") as "date", SUM(num_items_sold), COUNT(order_id), SUM(net_total), SUM(tax_total), SUM(total_sales) '
            'FROM wp_wc_order_stats '
            ' WHERE DATE_FORMAT(date_created, "%Y-%m-%d") between "' + min_date + '" AND "' + max_date +
            '" AND `status` IN ("wc-completed","wc-problem","wc-on-hold","wc-wyslane","wc-refunded","wc-processing")  group by DATE_FORMAT(date_created, "%Y-%m")')

        DBcursor = DronyWPDB.cursor()
        DBcursor.execute(Query)
        rows = DBcursor.fetchall()
        return rows

    def getBarChartQuater(self, min_date, max_date):
        DronyWPDB = baseLocal()
        Query = (
            'SELECT  CONCAT(YEAR(date_created),"-Q",QUARTER(date_created)) as "date", SUM(num_items_sold), COUNT(order_id),  SUM(net_total), SUM(tax_total), SUM(total_sales) '
            'FROM wp_wc_order_stats '
            ' WHERE DATE_FORMAT(date_created, "%Y-%m-%d") between "' + min_date + '" AND "' + max_date +
            '" AND `status` IN ("wc-completed","wc-problem","wc-on-hold","wc-wyslane","wc-refunded","wc-processing") group BY QUARTER(date_created), year(date_created) order by date ASC' )

        DBcursor = DronyWPDB.cursor()
        DBcursor.execute(Query)
        rows = DBcursor.fetchall()
        return rows

    def getBarChartYears(self, min_date, max_date):
        DronyWPDB = baseLocal()
        Query = (
            'SELECT  YEAR(date_created) as "date", SUM(num_items_sold), COUNT(order_id), SUM(net_total), SUM(tax_total), SUM(total_sales) '
            'FROM wp_wc_order_stats '
            ' WHERE DATE_FORMAT(date_created, "%Y-%m-%d") between "' + min_date + '" AND "' + max_date +
            '" AND `status` IN ("wc-completed","wc-problem","wc-on-hold","wc-wyslane","wc-refunded","wc-processing")  group BY year(date_created) order by date ASC' )

        DBcursor = DronyWPDB.cursor()
        DBcursor.execute(Query)
        rows = DBcursor.fetchall()
        return rows

    # def getOne(self, Id):
    #     self.data = Directories.select().where(Directories.Id == Id).execute()
    #     return self.data
    #
    #
    # def createOne(self,insert_dict):
    #     self.data =  Directories.insert(insert_dict).execute()
    #     return self.data
    def getAllOrders(self):
        date_start = date.today() + relativedelta(months=-1)
        date_end = date.today()

        DronyWPDB = baseWP()
        QueryOrdersTotal = ('SELECT * FROM wp_wc_order_stats '
                 'WHERE date_created BETWEEN "' + str(date_start) + ' 00:00:00" AND "' + str(
            date_end) + ' 23:59:59" AND returning_customer IS NOT null AND `status` IN ("wc-completed","wc-problem","wc-on-hold","wc-wyslane","wc-refunded","wc-processing")    ')

        DBcursor = DronyWPDB.cursor()
        DBcursor.execute(QueryOrdersTotal)
        rowsTotal = DBcursor.fetchall()
        rowsProducts = DBcursor.fetchall()
        dfOrdersTotal = DataFrame.from_records(rowsTotal, columns=['order_id', 'parent_id', 'date_created', 'date_created_gmt',
                                                   'num_items_sold', 'tax_total', 'shipping_total', 'net_total',
                                                   'returning_customer', 'status', 'customer_id', 'total_sales'])
        return dfOrdersTotal, date_start, date_end

    def getAllProductsOrders(self):
        date_start = date.today() + relativedelta(months=-1)
        date_end = date.today()

        DronyWPDB = baseWP()

        QueryOrdersProducts = ('SELECT * FROM wp_wc_order_product_lookup '
                               'WHERE date_created BETWEEN "' + str(date_start) + ' 00:00:00" AND "' + str(
            date_end) + ' 23:59:59"')

        DBcursor = DronyWPDB.cursor()
        DBcursor.execute(QueryOrdersProducts)
        rowsProducts = DBcursor.fetchall()
        dfOrdersProducts = DataFrame.from_records(rowsProducts,
                                                  columns=['order_item_id','order_id', 'product_id', 'variation_id', 'customer_id',
                                                           'date_created',
                                                           'product_qty', 'product_net_revenue',
                                                           'product_gross_revenue', 'coupon_amount',
                                                           'tax_amount', 'shipping_amount', 'shipping_tax_amount'])
        return dfOrdersProducts

    def refreshAll(self):
        totalOrders = self.getAllOrders()[0]
        productsOrders= self.getAllProductsOrders()

        WpWcOrderStats.objects.filter(date_created__range=[str(self.getAllOrders()[1]) + ' 00:00:00',
                                                           str(self.getAllOrders()[2]) + ' 23:59:59']).delete()
        WpWcOrderProductLookup.objects.filter(date_created__range=[str(self.getAllOrders()[1]) + ' 00:00:00',
                                                           str(self.getAllOrders()[2]) + ' 23:59:59']).delete()
        json_list = json.loads(json.dumps(list(totalOrders.T.to_dict().values()), default=str))
        json_list1 = json.loads(json.dumps(list(productsOrders.T.to_dict().values()), default=str))
        for dic1 in json_list1:
            print(dic1)
            WpWcOrderProductLookup.objects.create(**dic1)
        for dic in json_list:
            print(dic)
            WpWcOrderStats.objects.create(**dic)