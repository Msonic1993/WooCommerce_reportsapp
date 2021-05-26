import json
from datetime import date

from dateutil.relativedelta import relativedelta
from django.db.models import Sum, Func
from django.db.models.functions import Concat
from django.forms import model_to_dict
from django.utils.datetime_safe import datetime
from pandas import DataFrame

from reportsapp.database_repository.models import WpWcOrderStats
from reportsapp.database_repository.database import baseLocal, baseWP


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 2)'


class GeoOrdersRepository():

    def getGeoChart(self):
        DronyWPDB = baseWP()
        self.data = (
                'SELECT p.post_id, p.meta_key,  LEFT(`meta_value`, 256) as city , COUNT(`meta_value`), ROUND(SUM(o.net_total),2) FROM wp_postmeta p '
                'JOIN wp_wc_order_stats AS o ON o.order_id = p.post_id '
                ' WHERE p.meta_key = "_shipping_city"'
                ' GROUP BY city ORDER BY meta_key ASC  ')

        DBcursor = DronyWPDB.cursor()
        DBcursor.execute(self.data)
        rows = DBcursor.fetchall()
        products_list = rows
        return products_list


    def getAll(self):
        DronyWPDB = baseWP()
        self.data = (
                'SELECT p.post_id, p.meta_key,  LEFT(`meta_value`, 256) as city , COUNT(`meta_value`) as ilosc, ROUND(SUM(o.net_total),2) as wartość_netto FROM wp_postmeta p '
                'JOIN wp_wc_order_stats AS o ON o.order_id = p.post_id '
                ' WHERE p.meta_key = "_shipping_city"'
                ' GROUP BY city ORDER BY ilosc DESC  ')

        DBcursor = DronyWPDB.cursor(dictionary=True)
        DBcursor.execute(self.data)
        rows = DBcursor.fetchall()
        products_list = rows
        return products_list