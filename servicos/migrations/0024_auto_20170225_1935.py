# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-25 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0023_medicamento_id_medicamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='id_medicamento',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
