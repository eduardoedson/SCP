# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-13 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_auto_20170201_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='primeiro_telefone',
            field=models.CharField(max_length=50, verbose_name='Primeiro Telefone'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='segundo_telefone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Segundo Telefone'),
        ),
        migrations.DeleteModel(
            name='Telefone',
        ),
    ]