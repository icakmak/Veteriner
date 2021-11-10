from django.urls import path
from VetApps.Apps import views as api_views

urlpatterns = [
    path('sahipler/',api_views.CustomerListCreateAPIView.as_view(),name='sahip-listesi'),
    path('turler/',api_views.KindListCreateAPIView.as_view(),name='turler-listesi'),
    path('hayvanlar/<int:pk>',api_views.AnimalListCreateAPIView.as_view(),name='hayvan-listesi')
]