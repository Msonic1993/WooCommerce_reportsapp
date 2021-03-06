# Generated by Django 3.2a1 on 2021-03-23 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportsapp', '0015_auto_20210322_1220'),
    ]

    operations = [

        migrations.CreateModel(
            name='ProductPrices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_id', models.IntegerField(null=True)),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('unit_price', models.FloatField(null=True)),
                ('date', models.DateField(null=True, verbose_name=['%Y-%m-%d'])),
            ],
            options={
                'db_table': 'reportsapp_product_prices',
                'managed': True,
            },
        )
    ]
