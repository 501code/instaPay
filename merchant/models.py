from django.db import models


class SpaceShip(models.Model):
    model = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(max_digits=99, decimal_places=2)
