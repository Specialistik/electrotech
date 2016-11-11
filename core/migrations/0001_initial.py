# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 02:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=80, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('keywords', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('url', models.CharField(blank=True, max_length=80, null=True, verbose_name='\u0427\u0435\u043b\u043e\u0432\u0435\u043a\u043e-\u043f\u043e\u043d\u044f\u0442\u043d\u044b\u0439 URL')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='media/category')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Category', verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
            options={
                'db_table': 'categories',
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=80, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('keywords', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('url', models.CharField(blank=True, max_length=80, null=True, verbose_name='\u0427\u0435\u043b\u043e\u0432\u0435\u043a\u043e-\u043f\u043e\u043d\u044f\u0442\u043d\u044b\u0439 URL')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='media/product')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
            options={
                'db_table': 'products',
                'verbose_name': '\u0422\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b',
            },
        ),
    ]