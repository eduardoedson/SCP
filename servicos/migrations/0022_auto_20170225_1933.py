# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-25 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0021_auto_20170225_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='laboratorio',
            field=models.TextField(verbose_name='Laboratório'),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='nome',
            field=models.TextField(verbose_name='Nome'),
        ),
    ]
