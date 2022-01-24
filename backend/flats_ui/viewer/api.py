from rest_framework import status

from flats_ui.viewer.models import FlatOffer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class SetAsIgnoreApi(APIView):
    def get(self, request: Request):
        offer_id = request.query_params.get('id')
        offer = FlatOffer.objects.get(id=offer_id)

        offer.ignore = True
        offer.save()

        return Response('ok', status=status.HTTP_200_OK)


class SetAsFavouriteApi(APIView):
    def get(self, request):
        offer_id = request.query_params.get('id')
        offer = FlatOffer.objects.get(id=offer_id)

        offer.favourite = True
        offer.save()

        return Response('ok', status=status.HTTP_200_OK)
