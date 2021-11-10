from rest_framework import serializers
from VetApps.models import Customer,Kind,Animal

# from datetime import datetime,date
# from django.utils.timesince import timesince

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'

class KindSerializer(serializers.ModelSerializer):
    class Meta:
        model=Kind
        fields='__all__'

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Animal
        fields='__all__'

