from rest_framework import serializers
from VetApps.models import Customer,Kind,Animal

# from datetime import datetime,date
# from django.utils.timesince import timesince





class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Animal
        fields='__all__'

class CustomerSerializer(serializers.ModelSerializer):
    hayvanlari=serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='hayvan-detail' # 'hayvan-detail' urls deki name alanındaki veriyi yazıyoruz
        
    )
    
    class Meta:
        model = Customer
        fields = '__all__'
        
class KindSerializer(serializers.ModelSerializer):
    turler=serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='hayvan-detail' # 'tur-detail' urls deki name alanındaki veriyi yazıyoruz
        
    )
    class Meta:
        model=Kind
        fields='__all__'