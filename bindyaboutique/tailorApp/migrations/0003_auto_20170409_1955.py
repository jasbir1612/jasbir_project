# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tailorApp', '0002_auto_20170409_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodymeasurements',
            name='due_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
