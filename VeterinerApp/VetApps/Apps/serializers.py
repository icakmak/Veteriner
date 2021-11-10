from rest_framework import serializers
from VetApps.models import Customer,Kind,Animal

# from datetime import datetime,date
# from django.utils.timesince import timesince





class AnimalSerializer(serializers.ModelSerializer):
    animalCustomer=serializers.StringRelatedField()
    animalKind=serializers.StringRelatedField()
    class Meta:
        model=Animal
        fields=['animalName','animalPhoto','animalBirthdate','animalCustomer','animalKind']

class CustomerSerializer(serializers.ModelSerializer):
    sahipler=serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='hayvanlar-detail' # 'hayvan-detail' urls deki name alanındaki veriyi yazıyoruz
        
    )
    # hayvanlari=AnimalSerializer(many=True,read_only=True)
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