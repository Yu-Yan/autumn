# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autumn', '0002_author_content_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='content_type',
        ),
    ]
