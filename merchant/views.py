import json

from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.views.generic.base import View

from .models import SpaceShip, Payment


class SpaceShipListView(ListView):
    model = SpaceShip


class SpaceShipPayment(View):
    def get(self, request, *args, **kwargs):
        """
        Get the item_id and phone_number from the QR code client to create a new payment
        :param request:
        :param args:
        :param kwargs:
        :return: a JSON response indicating failure or success
        """
        try:
            phone_number = request.GET.get('phone_number', None)
            item_id = request.GET.get('item_id', None)
            # make a payment
            item = SpaceShip.objects.get(id=item_id)
            payment = Payment.objects.create(phone_number=phone_number, item=item)
            message = str(payment.id)
            status_code = 0
        except Exception as e:
            message = str(e)
            status_code = -1
        return JsonResponse({'message': message, 'status_code': status_code})

    def post(self, request, *args, **kwargs):
        """
        This is callback view that listens to responses from Beyonic when the user has made a payment
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = json.loads(request.body)
        try:
            remote_id = data['data']['collection_request']['id']
            payment = Payment.objects.get(remote_id=remote_id)
            payment.status = data['data']['status']
        except KeyError as e:
            pass  # TODO: something
        return HttpResponse('ok')

