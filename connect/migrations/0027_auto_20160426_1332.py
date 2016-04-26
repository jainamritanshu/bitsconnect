# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0026_auto_20160422_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='misc_no',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('desig', models.CharField(max_length=100)),
                ('num', models.IntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course',
            name='c_id',
            field=models.CharField(default=0, max_length=6),
            preserve_default=True,
        ),
    ]
