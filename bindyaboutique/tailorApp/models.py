from django.db import models

# Create your models here.

class BodyMeasurements(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120, blank=False, null=False)
    due_date = models.DateField(auto_now_add=False, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    length = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    Cross_Chest = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    Chest = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    Waist = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    Hipp = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    Armhole = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    Shoulder = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    Neck = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    Sleeves = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    Salwar = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    Mori = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    Knee = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    Calf = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    Theigh = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    BLenght = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    BChest = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    BShoulder = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    BWaist = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    BWaist = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    BSleeves = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    BDaat_Point = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)

    def __unicode__(self):
        return self.id

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Body Measurement'
        verbose_name_plural = 'Body Measurements'
