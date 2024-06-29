from rest_framework import generics
from businness.models import Businness
from businness.serializers import BusinnessSerializer

#serializers = serve para serealizar os dados e entregar em (JSON)

class BusinessCreateListView(generics.ListAPIView):
    queryset = Businness.objects.all()
    serializer_class = BusinnessSerializer

    
