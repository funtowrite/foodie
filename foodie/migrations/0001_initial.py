# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('startTime', models.DateTimeField(verbose_name=b'date start')),
                ('endTime', models.DateTimeField(verbose_name=b'date end')),
                ('location', models.CharField(max_length=200)),
                ('eventId', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('eventCount', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('eventCount', 'name'),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='vendors',
            field=models.ManyToManyField(to='foodie.Vendor'),
            preserve_default=True,
        ),
    ]
