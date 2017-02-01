# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-01 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_auto_20170111_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30, verbose_name='Título')),
                ('descricao', models.CharField(max_length=30, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Usuário',
                'verbose_name_plural': 'Tipos de Usuários',
            },
        ),
        migrations.CreateModel(
            name='StatusChamado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30, unique=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Usuário',
                'verbose_name_plural': 'Tipos de Usuários',
            },
        ),
        migrations.AddField(
            model_name='chamado',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.StatusChamado', verbose_name='Status'),
        ),
    ]
