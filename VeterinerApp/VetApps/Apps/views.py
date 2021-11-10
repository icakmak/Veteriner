from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from VetApps.models import Customer,Kind,Animal
from VetApps.Apps.serializers import CustomerSerializer,KindSerializer,AnimalSerializer

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
#sahiplar başlangıç
class CustomerListCreateAPIView(APIView):
    def get(self, request):
        sahiplerk=Customer.objects.all()
        serializer=CustomerSerializer(sahiplerk, many=True,   context={'request': request}) 
        return Response(serializer.data)
    
    def post(self, request ):
        serializer=CustomerSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data,    status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST) 

class CustomerDetailApiView(APIView):
    def get_object(self,pk):
        sahip=get_object_or_404(Customer,pk=pk)
        return sahip
    
    def get(self,request,pk):
        sahip=self.get_object(pk=pk)
        serializer=CustomerSerializer(sahip,context={'request': request})
        return Response(serializer.data)
    
    def put(self, request,pk):
        sahip=self.get_object(pk=pk)
        serializer=CustomerSerializer(sahip,data=request.data) 
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        sahip=self.get_object(pk=pk)
        sahip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#turler başlangıç
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

class KindDetailApiView(APIView):
    def get_object(self,pk):
        turler=get_object_or_404(Kind,pk=pk)
        return turler
    
    def get(self,request,pk):
        tur=self.get_object(pk=pk)
        serializer=KindSerializer(tur,context={'request': request})
        return Response(serializer.data)
    
    def put(self, request,pk):
        turler=self.get_object(pk=pk)
        serializer=KindSerializer(turler,data=request.data) 
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        turler=self.get_object(pk=pk)
        turler.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#hayvanlar başlangıç
class AnimalListCreateAPIView(APIView):
    def get(self, request):
        hayvanlar=Animal.objects.all()
        serializer=AnimalSerializer(hayvanlar, many=True) 
        return Response(serializer.data)
    
    def post(self, request ):
        serializer=AnimalSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data,    status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST) 
    
class AnimalDetailApiView(APIView):
    def get_object(self,pk):
        hayvan=get_object_or_404(Animal,pk=pk)
        return hayvan
    
    def get(self,request,pk):
        hayvan=self.get_object(pk=pk)
        serializer=AnimalSerializer(hayvan)
        return Response(serializer.data)
    
    def put(self, request,pk):
        hayvan=self.get_object(pk=pk)
        serializer=AnimalSerializer(hayvan,data=request.data) 
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        hayvan=self.get_object(pk=pk)
        hayvan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)