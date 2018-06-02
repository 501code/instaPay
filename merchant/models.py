from django.db import models


class SpaceShip(models.Model):
    model = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(max_digits=99, decimal_places=2)
    currency = models.CharField(max_length=55, default='KES', blank=False, null=False)

    def __str__(self):
        return self.model


class Payment(models.Model):
    phone_number = models.CharField(max_length=50, blank=False, null=False)
    item = models.ForeignKey(SpaceShip, blank=False, null=False, on_delete=models.DO_NOTHING)
