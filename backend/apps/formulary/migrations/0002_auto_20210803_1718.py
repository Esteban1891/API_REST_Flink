# Generated by Django 3.1.6 on 2021-08-03 17:18

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulary',
            name='market_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=50),
        ),
    ]
