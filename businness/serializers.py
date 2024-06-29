from rest_framework import serializers
from businness.models import Businness

class BusinnessSeralizer(serializers.ModelSerializer):

    class Meta:
        model = Businness
        fields = '__all__'