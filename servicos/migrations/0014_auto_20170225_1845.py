# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-25 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0013_auto_20170225_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principio_ativo', models.CharField(max_length=50, verbose_name='Principio Ativo')),
                ('cnpj', models.CharField(max_length=18, verbose_name='CNPJ')),
                ('laboratorio', models.CharField(max_length=100, verbose_name='Laboratório')),
                ('codggrem', models.CharField(max_length=18, verbose_name='codggrem')),
                ('ean', models.CharField(max_length=18, verbose_name='ean')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('apresentacao', models.CharField(max_length=50, verbose_name='Apresentação')),
                ('preco_fabricacao', models.CharField(max_length=10, verbose_name='Preço Fabricação')),
                ('preco_comercial', models.CharField(max_length=10, verbose_name='Preço Comercial')),
                ('restricao_hospitalar', models.CharField(max_length=10, verbose_name='Restrição Hospitalar')),
            ],
            options={
                'verbose_name': 'Medicamento',
                'verbose_name_plural': 'Medicamentos',
            },
        ),
        migrations.AlterModelOptions(
            name='cid',
            options={'verbose_name': 'Cid', 'verbose_name_plural': 'Cids'},
        ),
    ]
