from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from VetApps.models import Customer,Kind,Animal
from VetApps.Apps.serializers import CustomerSerializer,KindSerializer,AnimalSerializer

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class CustomerListCreateAPIView(APIView):
    def get(self, request):
        sahipler=Customer.objects.all()
        serializer=CustomerSerializer(sahipler, many=True,   context={'request': request}) 
        return Response(serializer.data)
    
    def post(self, request ):
        serializer=CustomerSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data,    status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST) 

class KindListCreateAPIView(APIView):
    def get(self, request):
        turler=Kind.objects.all()
        serializer=KindSerializer(turler, many=True,   context={'request': request}) 
        return Response(serializer.data)
    
    def post(self, request ):
        serializer=KindSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data,    status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST) 

class AnimalListCreateAPIView(APIView):
    def get(self, request):
        hayvanlar=Animal.objects.all()
        serializer=AnimalSerializer(hayvanlar, many=True,   context={'request': request}) 
        return Response(serializer.data)
    
    def post(self, request ):
        serializer=AnimalSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data,    status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST) 