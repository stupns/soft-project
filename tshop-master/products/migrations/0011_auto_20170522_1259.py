# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20170521_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='related_product_type',
            field=models.CharField(choices=[('0', 'Price'), ('1', 'Manual')], default='1', max_length=1),
        ),
    ]
