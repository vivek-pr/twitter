# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweeter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('following', models.ManyToManyField(related_name='user_following', to=settings.AUTH_USER_MODEL, verbose_name='folowing')),
                ('folowers', models.ManyToManyField(related_name='user_followers', to=settings.AUTH_USER_MODEL, verbose_name='folowers')),
                ('user', models.ForeignKey(related_name='user_for_follower_and_following', to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
        ),
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('text', models.TextField(max_length=150, db_index=True, verbose_name=' tweets ')),
                ('created', models.DateField(auto_now_add=True, verbose_name=' creation time ')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name=' author ')),
            ],
        ),
    ]
