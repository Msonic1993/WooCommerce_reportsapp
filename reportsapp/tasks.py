import datetime
import json
from urllib.request import Request, urlopen
import pandas as pd
from background_task import background
from django.utils import timezone
from reportsapp.database_repository.models import Dollar_exchange_rate
from reportsapp.database_repository.orders import OrdersRepository
from background_task.models import Task
from reportsapp.database_repository.warehouse import WarehouseRepository
now = datetime.datetime.now()
date = datetime.datetime(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute)
date_now =datetime.date(year=now.year, month=now.month, day=now.day-1)

time_warehouse_scheduled_job= datetime.time(20, 58, 00, tzinfo=timezone.get_current_timezone())
aware_datetime_warehouse_scheduled_job = datetime.datetime.combine(date, time_warehouse_scheduled_job)




@background(schedule=1)
def orders_scheduled_job():
    print("orders_scheduled_job")
    OrdersRepository().getAllOrders()
    OrdersRepository().refreshAll()
    print('Job end ')



@background(schedule=aware_datetime_warehouse_scheduled_job)
def warehouse_scheduled_job():
    print("warehouse_scheduled_job")
    WarehouseRepository().CreateAllHistorical()
    request = Request("http://api.nbp.pl/api/exchangerates/rates/a/usd/" + str(date_now) + "/?format=json")
    response = urlopen(request)
    elevations = response.read()
    data = json.loads(elevations, )
    df = pd.json_normalize(data['rates'])
    print(df)
    json_list = json.loads(json.dumps(list(df.T.to_dict().values())))

    for dic in json_list:
        Dollar_exchange_rate.objects.get_or_create(table=dic['no'], date=dic['effectiveDate'],
                                                   average_exchange_rate=dic['mid'])
        print(dic)
    print('Job end ')


warehouse_scheduled_job(repeat=Task.DAILY,verbose_name="warehouse_scheduled_job1")
orders_scheduled_job(repeat=3600,verbose_name="orders_scheduled_job")