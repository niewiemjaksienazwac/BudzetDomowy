# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-31 02:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caegory_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('value', models.CharField(max_length=100)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Category')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='transactions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Transaction'),
        ),
    ]
