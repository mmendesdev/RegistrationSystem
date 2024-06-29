from rest_framework import generics
from businness.models import Businness
from businness.serializers import BusinnessSeralizer

#serializers = serve para serealizar os dados e entregar em (JSONS)

class BusinnessCreateListView(generics.ListAPIView):
    queryset = Businness.objects.all() #buscar todos os dados da tabela businnes
    serializer_class = BusinnessSeralizer


class BusinnessRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Businness.objects.all() #buscar todos os dados da tabela businnes
    serializer_class = BusinnessSeralizer