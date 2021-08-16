import uuid
from django.db import models


class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_column="car_id")
    name = models.CharField(max_length=64)
    miles_per_gallon = models.SmallIntegerField(null=True)
    cylinders = models.SmallIntegerField(null=True)
    displacement = models.SmallIntegerField(null=True)
    horsepower = models.SmallIntegerField(null=True)
    weight_in_lbs = models.SmallIntegerField(null=True)
    acceleration = models.SmallIntegerField(null=True)
    year = models.DateField(null=True)
    origin = models.CharField(max_length=64, null=True)
