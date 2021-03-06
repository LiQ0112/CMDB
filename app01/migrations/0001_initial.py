# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-22 03:52
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息表',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ContractClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='分类标题')),
            ],
            options={
                'verbose_name': '合同分类表',
            },
        ),
        migrations.CreateModel(
            name='ContractDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='合同标题')),
                ('date', models.DateField(verbose_name='签订时间')),
                ('person', models.CharField(max_length=32, verbose_name='签订人')),
                ('contractfile', models.FileField(upload_to='contract/', verbose_name='合同附件')),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.ContractClass', verbose_name='分类')),
            ],
            options={
                'verbose_name': '合同详情表',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='部门名称')),
                ('code', models.CharField(max_length=16, verbose_name='部门编号')),
            ],
            options={
                'verbose_name': '部门信息表',
            },
        ),
        migrations.CreateModel(
            name='EquipClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='分类标题')),
                ('code', models.IntegerField(verbose_name='分类编号')),
            ],
            options={
                'verbose_name': '设备分类表',
            },
        ),
        migrations.CreateModel(
            name='EquipInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='设备名称')),
                ('brand', models.CharField(max_length=32, verbose_name='品牌')),
                ('_type', models.CharField(max_length=64, verbose_name='型号')),
                ('SN', models.CharField(max_length=64, verbose_name='出厂编号')),
                ('date', models.DateField(verbose_name='采购日期')),
                ('price', models.FloatField(verbose_name='采购价格')),
                ('warranty', models.CharField(max_length=32, verbose_name='保修期')),
                ('remark', models.CharField(max_length=64, verbose_name='备注')),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.EquipClass', verbose_name='设备分类')),
            ],
            options={
                'verbose_name': '设备基础信息表',
            },
        ),
        migrations.CreateModel(
            name='EquipMaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='报修时间')),
                ('error_description', models.CharField(max_length=256, verbose_name='故障描述')),
                ('repairs', models.CharField(max_length=32, verbose_name='报修人')),
                ('service_person', models.CharField(max_length=32, verbose_name='维修人')),
                ('service_result', models.CharField(max_length=128, verbose_name='维修结论')),
                ('service_cost', models.CharField(max_length=32, verbose_name='维修费用')),
                ('SN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.EquipInfo', verbose_name='出厂编号')),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.EquipClass', verbose_name='设备类型')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Department', verbose_name='使用部门')),
            ],
            options={
                'verbose_name': '设备维修表',
            },
        ),
        migrations.CreateModel(
            name='EquipState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='状态码')),
                ('title', models.CharField(max_length=32, verbose_name='状态标题')),
            ],
            options={
                'verbose_name': '状态表',
            },
        ),
        migrations.CreateModel(
            name='Organ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='机构名称')),
                ('code', models.CharField(max_length=32, verbose_name='机构代码')),
            ],
            options={
                'verbose_name': '机构信息表',
            },
        ),
        migrations.CreateModel(
            name='SupplierInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='厂商名称')),
                ('linkman', models.CharField(max_length=32, null=True, verbose_name='联系人')),
                ('pnone', models.CharField(max_length=11, verbose_name='联系电话')),
                ('address', models.CharField(max_length=128, verbose_name='地址')),
            ],
            options={
                'verbose_name': '厂商信息表',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='organ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Organ', verbose_name='机构'),
        ),
    ]
