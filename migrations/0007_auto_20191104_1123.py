# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-11-04 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sagenkarta-Admin', '0006_auto_20191030_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='changedate',
            field=models.DateTimeField(auto_now=True, verbose_name='Ändrad datum'),
        ),
    ]