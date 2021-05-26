from django.conf.urls import url
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from .views.costs_view import costs_post
from .views.detail_view import detail
from .views.fixed_costs_view import fixed_costs
from .views.geo_orders_view import geo_orders_view
from .views.income_expenses_view import income_expenses
from .views.index import index
from .views.invoice_list import invoiceList
from .views.orders_view import total_orders
from .views.top_products_view import top_products
from .views.warehouse_view import warehouse_view
from .views.invoice_details import invoiceDetails

urlpatterns = [
    path('', index, name='index'),
    path('logout/',  LogoutView.as_view(template_name='logout.html'), name="login"),
    path('login/',LoginView.as_view(template_name='login.html'),name="login"),
    path("totalorders/", total_orders, name='total_orders'),
    path("incomevsexpenses/", income_expenses, name='income_expenses'),
    path("bestproducts/", top_products, name='top_products'),
    path("warehouse/", warehouse_view, name='warehouse_view'),
    path("geoorders/", geo_orders_view, name='geo_orders_view'),
    path("costs/",costs_post, name='costs_post'),
    path("invoice/",invoiceList, name='invoiceList'),
    path("fixedcosts/",fixed_costs, name='fixed_costs'),
    url(r'^costs/(\d+)/$', detail,{}, name='detail'),
    url(r'^invoice/(.+)/$', invoiceDetails,{}, name='invoiceDetails'),


]
