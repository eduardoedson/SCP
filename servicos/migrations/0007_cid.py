# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-25 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0006_auto_20170202_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='cid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid_id', models.CharField(max_length=10, verbose_name='Cid ID')),
                ('descricao', models.CharField(max_length=70, verbose_name='Descrição')),
            ],
        ),
    ]
