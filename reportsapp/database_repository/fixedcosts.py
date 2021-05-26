from django.db.models import Func

from reportsapp.database_repository.models import FixedCosts


class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 2)'
class FixedCostsRepository():

    def getAll(self,min_date, max_date):
        select_data = {"date":"DATE_FORMAT( date,'%%Y-%%m-%%d')"}
        self.data = FixedCosts.objects.filter(date__range=[min_date, max_date]).extra(select=select_data).values('date','name','quantity','value')

        return self.data
