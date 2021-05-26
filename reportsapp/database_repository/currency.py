from django.db.models import Func

from reportsapp.database_repository.models import Dollar_exchange_rate


class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 2)'
class CurrencyRepository():

    def getAll(self,date_cost):
        select_data = {"date":"DATE_FORMAT( date,'%%Y-%%m-%%d')"}
        self.data = Dollar_exchange_rate.objects.filter(date="2021-04-02").extra(select=select_data).values('average_exchange_rate')

        for row in self.data:
            return row['average_exchange_rate']
