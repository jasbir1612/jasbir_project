# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BodyMeasurements',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('due_date', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('length', models.DecimalField(max_digits=20, decimal_places=2)),
                ('Cross_Chest', models.DecimalField(max_digits=20, decimal_places=2)),
                ('Chest', models.DecimalField(max_digits=20, decimal_places=2)),
                ('Waist', models.DecimalField(max_digits=20, decimal_places=2)),
                ('Hipp', models.DecimalField(max_digits=20, decimal_places=2)),
                ('Armhole', models.DecimalField(max_digits=20, decimal_places=2)),
                ('Shoulder', models.DecimalField(max_digits=20, decimal_places=2)),
                ('Neck', models.DecimalField(max_digits=20, decimal_places=2)),
                ('Sleeves', models.DecimalField(max_digits=20, decimal_places=2)),
                ('Salwar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('Mori', models.DecimalField(max_digits=20, decimal_places=2)),
                ('Knee', models.DecimalField(max_digits=20, decimal_places=2)),
                ('Calf', models.DecimalField(max_digits=20, decimal_places=2)),
                ('Theigh', models.DecimalField(max_digits=20, decimal_places=2)),
                ('BLenght', models.DecimalField(max_digits=20, decimal_places=2)),
                ('BChest', models.DecimalField(max_digits=20, decimal_places=2)),
                ('BShoulder', models.DecimalField(max_digits=20, decimal_places=2)),
                ('BWaist', models.DecimalField(max_digits=20, decimal_places=2)),
                ('BSleeves', models.DecimalField(max_digits=20, decimal_places=2)),
                ('BDaat_Point', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
        ),
    ]
