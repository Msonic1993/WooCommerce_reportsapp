import json
from datetime import date

import pandas
from django.db.models import Func
import numpy as np
from pandas import DataFrame

from reportsapp.database_repository.database import baseWP
from reportsapp.database_repository.models import HistoricalWarehouse


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 2)'


class WarehouseRepository():


    def getAllLocalDB(self):
        select_data = {"date": "DATE_FORMAT( date,'%%Y-%%m-%%d')"}
        self.data = HistoricalWarehouse.objects.extra(select=select_data).values()
        list_result = [entry for entry in self.data]
        return list_result

    def getOneLocalDB(self,get_product_name):
        select_data = {"date": "DATE_FORMAT( date,'%%Y-%%m-%%d')"}
        self.data = HistoricalWarehouse.objects.extra(select=select_data).filter(product_name__contains=get_product_name).values()
        list_result = [entry for entry in self.data]
        return list_result


    def getAll(self):
        DronyWPDB = baseWP()
        self.data = ('SELECT p.post_title AS Name,cat.name  AS Category,'
                     'MAX(CASE WHEN meta.meta_key = "_price" THEN meta.meta_value END) as Price, '
                     'MAX(CASE WHEN meta.meta_key = "_stock" THEN meta.meta_value END) AS `Stock`, '
                     'MAX(CASE WHEN meta.meta_key = "_price" THEN meta.meta_value END)*MAX(CASE WHEN meta.meta_key = "_stock" THEN meta.meta_value END) AS stan_wartosc '
                     'FROM wp_posts AS p '
                     'JOIN wp_postmeta AS meta ON p.ID = meta.post_ID '
                     'LEFT JOIN '
                     '('
                     'SELECT pp.id, '
                     'GROUP_CONCAT(t.name SEPARATOR " > ") AS name '
                     'FROM wp_posts AS pp '
                     'JOIN wp_term_relationships tr ON pp.id = tr.object_id '
                     'JOIN wp_term_taxonomy tt ON tr.term_taxonomy_id = tt.term_taxonomy_id '
                     'JOIN wp_terms t ON tt.term_id = t.term_id '
                     '|| tt.parent = t.term_id '
                     'WHERE tt.taxonomy = "product_cat" '
                     'GROUP BY pp.id, tt.term_id '
                     ') cat ON p.id = cat.id '
                     'WHERE (p.post_type = "product" OR p.post_type = "product_variation") '
                     'AND meta.meta_key IN ("_sku", "_price", "_weight", "_stock","total_sales") '
                     'AND meta.meta_value is not NULL '
                     'GROUP BY p.ID '
                     'ORDER BY MAX(CASE WHEN meta.meta_key = "_stock" THEN meta.meta_value END) * 1 DESC')

        DBcursor = DronyWPDB.cursor(dictionary=True)
        DBcursor.execute(self.data)
        rows = DBcursor.fetchall()
        products_list = rows
        df = pandas.DataFrame(products_list, columns=['Name','Category','Price','Stock','stan_wartosc'])
        df.replace(to_replace=[None], value=np.nan, inplace=True)
        df['Price'] = df['Price'].replace(np.nan, 0)
        df['Stock'] = df['Stock'].replace(np.nan, 0)
        df['stan_wartosc'] = df['stan_wartosc'].replace(np.nan, 0)
        print(date.today())
        return products_list,df


    def CreateAllHistorical(self):
        current_data = date.today()
        df = self.getAll()[1]
        for dic in df.itertuples():
            print(dic)
            self.rows = HistoricalWarehouse(product_name=dic.Name, product_category=dic.Category,quantity=dic.Stock, Unit_price=dic.Price,stock_value=dic.stan_wartosc, date=current_data)
            self.rows.save()
        return self.rows




    def getOne(self,get_product_name):
        DronyWPDB = baseWP()
        self.data = ('SELECT p.post_title AS Name,cat.name  AS Category,'
                     'MAX(CASE WHEN meta.meta_key = "_stock" THEN meta.meta_value END) AS `Stock`, '
                     'MAX(CASE WHEN meta.meta_key = "_price" THEN meta.meta_value END) as Price, '
                     'MAX(CASE WHEN meta.meta_key = "_price" THEN meta.meta_value END)*MAX(CASE WHEN meta.meta_key = "_stock" THEN meta.meta_value END) AS stan_wartosc '
                     'FROM wp_posts AS p '
                     'JOIN wp_postmeta AS meta ON p.ID = meta.post_ID '
                     'LEFT JOIN '
                     '('
                     'SELECT pp.id, '
                     'GROUP_CONCAT(t.name SEPARATOR " > ") AS name '
                     'FROM wp_posts AS pp '
                     'JOIN wp_term_relationships tr ON pp.id = tr.object_id '
                     'JOIN wp_term_taxonomy tt ON tr.term_taxonomy_id = tt.term_taxonomy_id '
                     'JOIN wp_terms t ON tt.term_id = t.term_id '
                     '|| tt.parent = t.term_id '
                     'WHERE tt.taxonomy = "product_cat" '
                     'GROUP BY pp.id, tt.term_id '
                     ') cat ON p.id = cat.id '
                     'WHERE (p.post_type = "product" OR p.post_type = "product_variation" )'
                     'AND meta.meta_key IN ("_sku", "_price", "_weight", "_stock","total_sales") '
                     'AND meta.meta_value is not NULL '
                     'AND p.post_title like "%'+get_product_name+'%" '
                     'GROUP BY p.ID '
                     'ORDER BY MAX(CASE WHEN meta.meta_key = "_stock" THEN meta.meta_value END) * 1 DESC')

        DBcursor = DronyWPDB.cursor(dictionary=True)
        DBcursor.execute(self.data)
        rows = DBcursor.fetchall()
        products_list = rows
        return products_list




