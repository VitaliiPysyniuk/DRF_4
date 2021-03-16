from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class CarModel(models.Model):
    class Meta:
        db_table = 'car'

    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.IntegerField()
    price = models.IntegerField()
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, default=1, related_name='cars')
