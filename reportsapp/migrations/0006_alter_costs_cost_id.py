# Generated by Django 3.2a1 on 2021-02-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportsapp', '0005_alter_costs_date_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costs',
            name='cost_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
