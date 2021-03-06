# Generated by Django 3.2a1 on 2021-02-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportsapp', '0002_auto_20210224_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costs',
            name='cost_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='costs',
            name='date_cost',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='costs',
            name='net_total',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='costs',
            name='num_items_buy',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='costs',
            name='shipping_total',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='costs',
            name='tax_total',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='costs',
            name='total_buy',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='costs',
            name='unit_price',
            field=models.FloatField(null=True),
        ),
    ]
