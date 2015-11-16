# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_remove_shop_temporal_cant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shop_desc',
            name='shop',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]
