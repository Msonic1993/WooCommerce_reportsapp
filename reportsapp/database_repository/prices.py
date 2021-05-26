# import pandas
# from django.db.models import Func
# import numpy as np
# from reportsapp.database_repository.database import baseLocal, baseWP
#
#
# class Round(Func):
#     function = 'ROUND'
#     template = '%(function)s(%(expressions)s, 2)'
#
#
# class PricesRepository:
#
#     def getAll(self):
#         DronyWPDB = baseWP()
#         Query = (
#             'SELECT p.ID,'
#             'p.post_title AS Name, '
#             'IFNULL(MAX(CASE WHEN meta.meta_key = "_price" THEN meta.meta_value END),0) as Price '
#             'FROM wp_posts AS p '
#             'JOIN wp_postmeta AS meta ON p.ID = meta.post_ID '
#             'LEFT JOIN '
#             '('
#             'SELECT pp.id, '
#             'GROUP_CONCAT(t.name SEPARATOR " > ") AS name '
#             'FROM wp_posts AS pp '
#             'JOIN wp_term_relationships tr ON pp.id = tr.object_id '
#             'JOIN wp_term_taxonomy tt ON tr.term_taxonomy_id = tt.term_taxonomy_id '
#             'JOIN wp_terms t ON tt.term_id = t.term_id '
#             '|| tt.parent = t.term_id '
#             'WHERE tt.taxonomy = "product_cat" '
#             'GROUP BY pp.id, tt.term_id '
#             ')'
#             'cat ON p.id = cat.id '
#             'WHERE (p.post_type = "product" OR p.post_type = "product_variation") '
#             'AND meta.meta_key IN ("_sku", "_price", "_weight", "_stock","total_sales") '
#             'AND meta.meta_value is not NULL '
#             'GROUP BY p.ID '
#             'ORDER BY MAX(CASE WHEN meta.meta_key = "_stock" THEN meta.meta_value END) * 1 DESC')
#
#         DBcursor = DronyWPDB.cursor(dictionary=True)
#         DBcursor.execute(Query)
#         rows = DBcursor.fetchall()
#         products_list = rows
#         df = pandas.DataFrame(products_list, columns=['Name', 'Category', 'Price', 'Stock', 'stan_wartosc'])
#         df.replace(to_replace=[None], value=np.nan, inplace=True)
#         df['Price'] = df['Price'].replace(np.nan, 0)
#         df['Stock'] = df['Stock'].replace(np.nan, 0)
#         df['stan_wartosc'] = df['stan_wartosc'].replace(np.nan, 0)
#
#         return products_list
