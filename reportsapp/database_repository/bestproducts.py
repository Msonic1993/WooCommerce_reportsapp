from django.db.models import Func

from reportsapp.database_repository.database import baseWP

class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 2)'


class TopProductsRepository():

    def getAll(self,min_date, max_date,get_product_name):
        DronyWPDB = baseWP()
        self.data = (
                'SELECT DATE_FORMAT( op.date_created,"%Y-%m") AS date, post.post_title as name, sum(op.product_qty) AS quantity, sum(op.product_net_revenue) AS value, sum(op.product_net_revenue) / sum(op.product_qty) as unit_value '
                'FROM  wp_wc_order_product_lookup AS op '
                'JOIN wp_posts AS post ON post.ID = op.product_id '
                'JOIN wp_wc_order_stats as wwo ON wwo.order_id = op.order_id '
                'WHERE  DATE_FORMAT( op.date_created,"%Y-%m") between "' + min_date + '" and "' + max_date + '" AND wwo.`status` <> "wc-cancelled" and post.post_title like "%' + get_product_name + '%" group BY op.product_id, date ORDER BY   DATE DESC , quantity DESC')

        DBcursor = DronyWPDB.cursor(dictionary=True)
        DBcursor.execute(self.data)
        rows = DBcursor.fetchall()
        products_list = rows
        return products_list



    def getAllDate(self):
        DronyWPDB = baseWP()
        self.data = ('SELECT post.post_title, sum(op.product_qty) AS quantity, sum(op.product_net_revenue) AS value, sum(op.product_net_revenue) / sum(op.product_qty) as unit_value FROM  wp_wc_order_product_lookup AS op '
                     'JOIN wp_posts AS post ON post.ID = op.product_id '
                    'JOIN wp_wc_order_stats as wwo ON wwo.order_id = op.order_id '
                     'WHERE wwo.`status` <> "wc-cancelled" group BY op.product_id ORDER BY quantity DESC')

        DBcursor = DronyWPDB.cursor(dictionary=True)
        DBcursor.execute(self.data)
        rows = DBcursor.fetchall()
        products_list = rows

        return products_list