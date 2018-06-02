from django.urls import path

from merchant.views import SpaceShipListView

urlpatterns = [
    path('', SpaceShipListView.as_view(), name='spaceship-list'),
]