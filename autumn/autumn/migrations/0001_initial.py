# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('sig', models.CharField(max_length=150)),
                ('up_num', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('sub_title', models.CharField(max_length=255)),
                ('pub_date', models.DateField(auto_now=True)),
                ('content', models.TextField()),
                ('up_num', models.IntegerField(default=0)),
                ('author', models.ForeignKey(to='autumn.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=255)),
                ('pub_date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(to='autumn.Author')),
                ('blog', models.ForeignKey(to='autumn.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=255)),
                ('pub_date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(to='autumn.Author')),
                ('to_author', models.ForeignKey(related_name='message_to', to='autumn.Author')),
            ],
        ),
    ]
