# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_temporal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('cant', models.IntegerField()),
                ('product', models.ForeignKey(to='principal.Product', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='shop_temporaly',
            name='product',
        ),
        migrations.RemoveField(
            model_name='shop_temporaly',
            name='user',
        ),
        migrations.DeleteModel(
            name='Shop_temporaly',
        ),
    ]
