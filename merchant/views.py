from django.views.generic import ListView

from .models import SpaceShip


class SpaceShipListView(ListView):
    model = SpaceShip
