from django.urls import path

from merchant.views import SpaceShipListView, SpaceShipPayment
urlpatterns = [
    path('', SpaceShipListView.as_view(), name='spaceship-list'),
    path('payment', SpaceShipPayment.as_view(), name='merchant_payment')
]