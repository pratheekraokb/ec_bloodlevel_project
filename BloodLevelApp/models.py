# BloodLevelApp/models.py
from django.db import models

class BloodLevel(models.Model):
    bloodlevelId = models.AutoField(primary_key=True)
    blood_category = models.CharField(max_length=100)
    percentage_value = models.FloatField()

    def __str__(self):
        return f"{self.blood_category} - {self.percentage_value}%"
