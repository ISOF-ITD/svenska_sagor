# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-11-12 10:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sagenkarta-Admin', '0013_auto_20191111_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrowdSourceUsers',
            fields=[
                ('userid', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'crowdsource_users',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='records',
            name='istranscribed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='records',
            name='transcriptiondate',
            field=models.DateTimeField(blank=True, default='1900-01-01', verbose_name='Transkriptionsdatum'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='records',
            name='transcriptionstatus',
            field=models.CharField(choices=[('untranscribed', 'Ej transkriberad'), ('transcribed', 'Transkriberad'), ('reviewing', 'Under granskning'), ('approved', 'Godkänd'), ('published', 'Publicerad')], default='new', max_length=20),
        ),
        migrations.AddField(
            model_name='records',
            name='transcribedby',
            field=models.ForeignKey(blank=True, db_column='transcribedby', null=True, on_delete=django.db.models.deletion.CASCADE, to='Sagenkarta-Admin.CrowdSourceUsers'),
        ),
    ]
