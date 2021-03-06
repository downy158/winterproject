# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharespace', '0005_auto_20160228_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='address1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='space',
            name='address2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='space',
            name='address3',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='space',
            name='space_type',
            field=models.CharField(choices=[('THEATER', '소극장'), ('METTINGROOM', '회의실'), ('PARKING', '주차장')], default='THEATER', max_length=20),
        ),
    ]
