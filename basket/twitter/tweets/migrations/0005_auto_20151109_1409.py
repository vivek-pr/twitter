# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20151109_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweets',
            options={'ordering': ['-created']},
        ),
    ]
