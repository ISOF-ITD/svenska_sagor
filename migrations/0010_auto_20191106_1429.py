# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-11-06 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sagenkarta-Admin', '0009_auto_20191104_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personsplaces',
            name='changedate',
        ),
        migrations.RemoveField(
            model_name='personsplaces',
            name='createdate',
        ),
        migrations.RemoveField(
            model_name='personsplaces',
            name='createdby',
        ),
        migrations.RemoveField(
            model_name='personsplaces',
            name='editedby',
        ),
        migrations.RemoveField(
            model_name='recordsmetadata',
            name='changedate',
        ),
        migrations.RemoveField(
            model_name='recordsmetadata',
            name='createdate',
        ),
        migrations.RemoveField(
            model_name='recordsmetadata',
            name='createdby',
        ),
        migrations.RemoveField(
            model_name='recordsmetadata',
            name='editedby',
        ),
        migrations.AlterField(
            model_name='recordsmetadata',
            name='type',
            field=models.CharField(blank=True, choices=[('dialektkarta_titlar', 'Dialektkarta titlar'), ('filemaker_id', 'FileMaker ID'), ('questions', 'Frågor'), ('folkmusik_recorded_by', 'Inspelat eller inlämnat av'), ('folkmusik_genre', 'Låttyp eller visgenre'), ('matkarta_content', 'Matkarta innehåll'), ('folkmusik_medium', 'Medium'), ('folkmusik_proveniens', 'Proveniens'), ('folkmusik_published', 'Publiserad'), ('sitevision_url', 'Sitevison url'), ('folkmusik_instrument', 'Sång/instrument'), ('folkmusik_musician_name', 'Sångare/instrumentalist namn'), ('folkmusik_composer', 'Upphovsman melodi'), ('folkmusik_author_text', 'Upphovsman text'), ('folkmusik_comment', 'Övrigt')], max_length=30, null=True),
        ),
    ]
