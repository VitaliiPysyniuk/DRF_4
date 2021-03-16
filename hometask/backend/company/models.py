from django.db import models

from owner.models import OwnerModel
from .managers import CompanyManager


class CompanyModel(models.Model):
    class Meta:
        db_table = 'companies'

    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    owner = models.ForeignKey(OwnerModel, on_delete=models.SET_DEFAULT, default='', related_name='companies')

    objects = CompanyManager()
