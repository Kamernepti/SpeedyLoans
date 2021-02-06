from django.db import models
from datetime import datetime

        
class Applicant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    income = models.IntegerField()
    credit = models.IntegerField(null=False)
    employed = models.BooleanField(null=False)
    approved_amount = models.IntegerField(null=True, default=2)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

def __str__(self):
        return self.name