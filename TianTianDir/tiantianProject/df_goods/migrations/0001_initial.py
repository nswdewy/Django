# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gnumber', models.CharField(max_length=10)),
                ('gtitle', models.CharField(max_length=20)),
                ('gsubtitle', models.CharField(max_length=100)),
                ('gimage', models.ImageField(upload_to=b'goods/')),
                ('gdetail', tinymce.models.HTMLField()),
                ('gunit', models.CharField(max_length=20)),
                ('gprice', models.DecimalField(max_digits=20, decimal_places=2)),
                ('ginventory', models.IntegerField()),
                ('gsupplier', models.CharField(max_length=20)),
                ('gpurchase_date', models.DateField()),
                ('gseason', models.CharField(max_length=1)),
                ('gorigin', models.CharField(max_length=20)),
                ('gclick', models.IntegerField()),
                ('grecommend', models.IntegerField()),
                ('gadv', models.BooleanField(default=False)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ttitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='gtype',
            field=models.ForeignKey(to='df_goods.TypeInfo'),
        ),
    ]
