from business.models import Businness
from rest_framework import generics

from businness.serializers import BusinnessSeralizer

# serializers = serve para serealizar os dados e entregar em (JSONS)


class BusinnessCreateListView(generics.ListAPIView):
    queryset = Businness.objects.all()
    serializer_class = BusinnessSeralizer


class BusinnessRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Businness.objects.all()
    serializer_class = BusinnessSeralizer
