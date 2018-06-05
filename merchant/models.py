from django.db import models


class SpaceShip(models.Model):
    # Sample merchant product
    model = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(max_digits=99, decimal_places=2)
    currency = models.CharField(max_length=55, default='KES', blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(default='spaceship.jpg')

    def __str__(self):
        return self.model


class Payment(models.Model):
    """
    This is model to hold payment information. There's an on create signal to handle the actual payment process
    via the provider's API
    """
    NEW = 'new'
    REQUEST_SENT = 'request_sent'
    SUCCESS = 'success'
    FAILED = 'failed'
    PAYMENT_STATUSES = ((NEW, 'new'), (REQUEST_SENT, 'request_sent'), (SUCCESS, 'success'), (FAILED, 'failed'))

    phone_number = models.CharField(max_length=50, blank=False, null=False)
    # item is tied to the merchant product. In a real scenario this should support different types of items
    item = models.ForeignKey(SpaceShip, blank=False, null=False, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUSES, default=NEW)
    # request_response is a simple way to log our API responses when a payment is made
    request_response = models.TextField(null=True, blank=True)
    # remote_id will store the reference from the payment provider
    remote_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.item) + ' ' + str(self.phone_number)

