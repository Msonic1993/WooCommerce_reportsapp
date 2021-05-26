import json
from datetime import date

from dateutil.relativedelta import relativedelta
from django.db.models import Sum, Func, Subquery, OuterRef, Count
from django.db.models.functions import Concat
from django.forms import model_to_dict
from django.utils.datetime_safe import datetime
from pandas import DataFrame

from reportsapp.database_repository.models import WpWcOrderStats, WpWcOrderProductLookup
from reportsapp.database_repository.database import baseLocal, baseWP


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 2)'


class ProductsRepository:

    def getAll(self):
        DronyWPDB = baseWP()
        Query = (
                'SELECT p.post_title as name FROM wp_posts p '
                ' LEFT JOIN wp_postmeta pm1 ON pm1.post_id = p.ID'
                ' LEFT JOIN wp_term_relationships AS tr ON tr.object_id = p.ID'
                ' JOIN wp_term_taxonomy AS tt ON tt.taxonomy = "product_cat" AND tt.term_taxonomy_id = tr.term_taxonomy_id '
                ' JOIN wp_terms AS t ON t.term_id = tt.term_id'
                ' WHERE p.post_type in("product", "product_variation") AND p.post_status = "publish" AND p.post_content <> ""'
                ' GROUP BY p.ID,p.post_title')

        DBcursor = DronyWPDB.cursor(dictionary=True)
        DBcursor.execute(Query)

        rows = DBcursor.fetchall()

        return rows