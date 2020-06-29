# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-26 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_equipallot'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipScrap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='设备名称')),
                ('SN', models.CharField(max_length=64, verbose_name='出厂编号')),
                ('buy_date', models.DateField(verbose_name='采购日期')),
                ('scrap_date', models.DateField(verbose_name='报废日期')),
                ('price', models.FloatField(verbose_name='采购价格')),
                ('warranty', models.CharField(max_length=32, verbose_name='保修期')),
                ('remark', models.CharField(max_length=64, null=True, verbose_name='备注')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.EquipClass', verbose_name='设备分类')),
                ('depart', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app01.Department', verbose_name='使用部门')),
                ('supllier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.SupplierInfo', verbose_name='采购厂商')),
            ],
            options={
                'verbose_name': '资产报废表',
            },
        ),
    ]