# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
                ('name', models.CharField(max_length=50)),
                ('name_proposal', models.CharField(max_length=50)),
            ],
        ),
    ]
