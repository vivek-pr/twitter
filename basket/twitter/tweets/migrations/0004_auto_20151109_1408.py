# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_auto_20151109_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='created',
            field=models.DateTimeField(verbose_name=' creation time ', auto_now_add=True),
        ),
    ]
