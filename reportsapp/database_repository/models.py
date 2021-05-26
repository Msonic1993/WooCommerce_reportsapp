# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.forms import forms

from znowodronach_reports import settings


class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'




class SitetreeTree(models.Model):
    title = models.CharField(max_length=100)
    alias = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'sitetree_tree'


class SitetreeTreeitem(models.Model):
    title = models.CharField(max_length=100)
    hint = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    urlaspattern = models.IntegerField()
    hidden = models.IntegerField()
    alias = models.CharField(max_length=80, blank=True, null=True)
    description = models.TextField()
    inmenu = models.IntegerField()
    inbreadcrumbs = models.IntegerField()
    insitetree = models.IntegerField()
    access_loggedin = models.IntegerField()
    access_guest = models.IntegerField()
    access_restricted = models.IntegerField()
    access_perm_type = models.IntegerField()
    sort_order = models.IntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    tree = models.ForeignKey(SitetreeTree, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sitetree_treeitem'
        unique_together = (('tree', 'alias'),)


class SitetreeTreeitemAccessPermissions(models.Model):
    treeitem = models.ForeignKey(SitetreeTreeitem, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sitetree_treeitem_access_permissions'
        unique_together = (('treeitem', 'permission'),)




class WpWcOrderStats(BaseModel):
    order_id = models.PositiveBigIntegerField(primary_key=True)
    parent_id = models.PositiveBigIntegerField()
    date_created = models.DateTimeField()
    date_created_gmt = models.DateTimeField()
    num_items_sold = models.IntegerField()
    tax_total = models.FloatField()
    shipping_total = models.FloatField()
    net_total = models.FloatField()
    returning_customer = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=200)
    customer_id = models.PositiveBigIntegerField()
    total_sales = models.FloatField()


    class Meta:
        managed = False
        db_table = 'wp_wc_order_stats'


class WpWcOrderProductLookup(BaseModel):
    order_item_id = models.PositiveBigIntegerField(primary_key=True)
    order_id = models.PositiveBigIntegerField()
    product_id = models.PositiveBigIntegerField()
    variation_id = models.PositiveBigIntegerField()
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    product_qty = models.IntegerField()
    product_net_revenue = models.FloatField()
    product_gross_revenue = models.FloatField()
    coupon_amount = models.FloatField()
    tax_amount = models.FloatField()
    shipping_amount = models.FloatField()
    shipping_tax_amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'wp_wc_order_product_lookup'



class Costs(BaseModel):
    id = models.AutoField(primary_key=True)
    invoice_no = models.CharField(max_length=200,null=True)
    cost_name = models.CharField(max_length=200,null=True)
    date_cost = models.DateField(settings.DATE_INPUT_FORMATS,null=True)
    num_items_buy = models.IntegerField(null=True)
    unit_price_usd =models.FloatField(null=True)
    tax_total_usd = models.FloatField(null=True)
    shipping_total_usd = models.FloatField(null=True)
    shipping_per_unit_usd =models.FloatField(null=True)
    net_total_usd = models.FloatField(null=True)
    total_buy_usd = models.FloatField(null=True)
    unit_price = models.FloatField(null=True)
    tax_total = models.FloatField(null=True)
    shipping_total = models.FloatField(null=True)
    shipping_per_unit = models.FloatField(null=True)
    net_cost_usd = models.FloatField(null=True)
    net_cost_pln = models.FloatField(null=True)
    net_total = models.FloatField(null=True)
    total_buy = models.FloatField(null=True)
    unit_cost = models.FloatField(null=True)
    unit_cost_pln = models.FloatField(null=True)


class Dollar_exchange_rate(BaseModel):
    id = models.AutoField(primary_key=True)
    table = models.CharField(max_length=200,null=True)
    date = models.DateField(settings.DATE_INPUT_FORMATS,null=True)
    average_exchange_rate = models.FloatField(null=True)

    class Meta:
        managed = False
        db_table = 'dollar_exchange_rate'



class FixedCosts(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,null=True)
    date = models.DateField(settings.DATE_INPUT_FORMATS,null=True)
    quantity = models.IntegerField(null=True)
    value = models.FloatField(null=True)

    class Meta:
        managed = True
        db_table = 'reportsapp_fixedcosts'


class HistoricalWarehouse(BaseModel):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200,null=True)
    product_category = models.CharField(max_length=200, null=True)
    quantity = models.FloatField(null=True)
    Unit_price = models.FloatField(null=True)
    stock_value = models.FloatField(null=True)
    date = models.DateField(settings.DATE_INPUT_FORMATS, null=True)

    class Meta:
        managed = True
        db_table = 'reportsapp_historical_warehouse'


class ProductPrices(BaseModel):
    id = models.AutoField(primary_key=True)
    product_id = models.IntegerField(null=True)
    product_name = models.CharField(max_length=200,null=True)
    unit_price = models.FloatField(null=True)
    date = models.DateField(settings.DATE_INPUT_FORMATS, null=True)

    class Meta:
        managed = True
        db_table = 'reportsapp_product_prices'



class Documents(BaseModel):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='media/documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)