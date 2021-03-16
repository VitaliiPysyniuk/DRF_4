from django.db import models

from company.models import CompanyModel
from .managers import EmployeeManager


class EmployeeModel(models.Model):
    class Meta:
        db_table = 'employees'

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    profession = models.CharField(max_length=25)
    age = models.IntegerField()
    is_employed = models.BooleanField()
    company = models.ForeignKey(CompanyModel, on_delete=models.SET_DEFAULT, default='', null=True, related_name='employees')

    objects = EmployeeManager()
