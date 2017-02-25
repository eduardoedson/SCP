# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-25 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0007_cid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cid',
            name='cid_id',
            field=models.CharField(max_length=10, unique=True, verbose_name='Cid ID'),
        ),
        migrations.AlterField(
            model_name='cid',
            name='descricao',
            field=models.CharField(max_length=70, unique=True, verbose_name='Descrição'),
        ),
    ]
