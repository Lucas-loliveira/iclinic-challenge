from django.db import models

class Prescription(models.Model):
    id_clinic = models.PositiveIntegerField()
    id_physician = models.PositiveIntegerField(blank=False, null=False)
    id_patient = models.PositiveIntegerField(blank=False, null=False)
    text = models.CharField(max_length = 300, blank=False, null=False)
