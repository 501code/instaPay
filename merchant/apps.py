from django.apps import AppConfig


class MerchantConfig(AppConfig):
    name = 'merchant'

    def ready(self):
        import merchant.signals