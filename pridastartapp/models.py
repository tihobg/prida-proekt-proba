from django.db import models


class Patients(models.Model):
    patient_id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    years = models.PositiveIntegerField(blank=True, null=True)
    probe_date = models.DateField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    arterial_pressure = models.CharField(max_length=20, blank=True, null=True)
    gw = models.IntegerField(blank=True, null=True)
    baby_weight = models.IntegerField(blank=True, null=True)
    erythrocytes = models.FloatField(blank=True, null=True)
    hemoglobin = models.FloatField(blank=True, null=True)
    #

    def __str__(self):
        return self.name


# Create your models here.
