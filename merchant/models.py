from django.db import models


class SpaceShip(models.Model):
    model = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(max_digits=99, decimal_places=2)
    currency = models.CharField(max_length=55, default='KES', blank=False, null=False)

    def __str__(self):
        return self.model


class Payment(models.Model):
    NEW = 'new'
    REQUEST_SENT = 'request_sent'
    SUCCESS = 'success'
    FAILED = 'failed'
    PAYMENT_STATUSES = ((NEW, 'new'), (REQUEST_SENT, 'request_sent'), (SUCCESS, 'success'), (FAILED, 'failed'))

    phone_number = models.CharField(max_length=50, blank=False, null=False)
    item = models.ForeignKey(SpaceShip, blank=False, null=False, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUSES, default=NEW)
    request_response = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.item) + ' ' + str(self.phone_number)
