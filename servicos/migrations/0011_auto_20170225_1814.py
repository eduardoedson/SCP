# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-25 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0010_auto_20170225_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cid',
            name='descricao',
            field=models.CharField(max_length=250, unique=True, verbose_name='Descrição'),
        ),
    ]