from django.db.models import Count, Sum

from reportsapp.database_repository.database import baseLocal
from reportsapp.database_repository.models import Costs


class InvoiceRepository():
    select_data = {"date_cost": "DATE_FORMAT( date_cost,'%%Y-%%m-%%d')"}

    def getAll(self):
        DronyWPDB = baseLocal()
        self.data = 'SELECT invoice_no, DATE_FORMAT( date_cost,"%Y-%m-%d") as date_cost, ROUND(sum(total_buy),2) as `total_buy` FROM reportsapp_costs GROUP BY invoice_no ORDER BY date_cost DESC'

        DBcursor = DronyWPDB.cursor(dictionary=True)
        DBcursor.execute(self.data)
        rows = DBcursor.fetchall()
        products_list = rows
        return products_list

    def getDetails(self, min_date, max_date,invoice_no):
        self.data = Costs.objects.extra(select=self.select_data).filter(date_cost__range=(min_date, max_date), invoice_no=invoice_no).order_by(
            '-date_cost')
        return self.data