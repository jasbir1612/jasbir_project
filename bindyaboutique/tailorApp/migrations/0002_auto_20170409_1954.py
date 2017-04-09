# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tailorApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bodymeasurements',
            options={'verbose_name': 'Body Measurement', 'verbose_name_plural': 'Body Measurements'},
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='Armhole',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='BChest',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='BDaat_Point',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='BLenght',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='BShoulder',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='BSleeves',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='BWaist',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='Calf',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='Chest',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='Cross_Chest',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='Hipp',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='Knee',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='Mori',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='Neck',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='Salwar',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='Shoulder',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='Sleeves',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='Theigh',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='Waist',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='description',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='due_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurements',
            name='length',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
    ]
