# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20151115_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop_temporal',
            name='cant',
        ),
    ]
