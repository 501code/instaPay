from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from .models import Payment


@receiver(post_save, sender=Payment)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Initiate a Beyonic Collection Request to request money from the user
        beyonic.api_key = settings.BEYONIC_API_KEY
        beyonic.CollectionRequest.create(
            phonenumber=instance.phone_number,
            amount=instance.item.price,
            currency=instance.item.currency,
            description='Payment for ' + instance.item.model,
            callback_url=reverse('merchant_payment'),
            send_instructions=True
        )
