# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-25 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0014_auto_20170225_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='principio_ativo',
            field=models.CharField(max_length=100, verbose_name='Principio Ativo'),
        ),
    ]
