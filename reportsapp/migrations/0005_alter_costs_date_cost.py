# Generated by Django 3.2a1 on 2021-02-25 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportsapp', '0004_alter_costs_date_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costs',
            name='date_cost',
            field=models.DateField(null=True, verbose_name=['%Y-%m-%d']),
        ),
    ]
