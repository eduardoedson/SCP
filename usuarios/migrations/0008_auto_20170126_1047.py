# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-26 10:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20170125_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='especialidademedico',
            old_name='descricao',
            new_name='especialidade',
        ),
    ]