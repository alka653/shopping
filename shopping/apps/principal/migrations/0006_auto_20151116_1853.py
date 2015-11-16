# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_shop_desc_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop_desc',
            name='cant',
        ),
        migrations.RemoveField(
            model_name='shop_desc',
            name='price',
        ),
    ]
