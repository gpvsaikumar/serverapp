# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task3app', '0002_auto_20171006_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='url',
            field=models.ImageField(upload_to=b''),
        ),
    ]