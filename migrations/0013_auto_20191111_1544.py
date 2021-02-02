# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-11-11 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sagenkarta-Admin', '0012_auto_20191107_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordsmetadata',
            name='type',
            field=models.CharField(blank=True, choices=[('dialektkarta_titlar', 'Dialektkarta titlar'), ('filemaker_id', 'FileMaker ID'), ('questions', 'Frågor'), ('folkmusik_recorded_by', 'Inspelat eller inlämnat av'), ('folkmusik_genre', 'Låttyp eller visgenre'), ('matkarta_content', 'Matkarta innehåll'), ('folkmusik_medium', 'Medium'), ('folkmusik_proveniens', 'Proveniens'), ('folkmusik_published', 'Publiserad'), ('sitevision_url', 'Sitevison url'), ('folkmusik_instrument', 'Sång/instrument'), ('folkmusik_musician_name', 'Sångare/instrumentalist namn'), ('folkmusik_composer', 'Upphovsman melodi'), ('folkmusik_author_text', 'Upphovsman text'), ('test', 'testaren'), ('folkmusik_comment', 'Övrigt')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sockenv1',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]