from django.urls import path
from VetApps.Apps import views as api_views

urlpatterns = [
    path('sahipler/',api_views.CustomerListCreateAPIView.as_view(),name='sahipler-listesi'),
    path('sahip/<int:pk>',api_views.CustomerDetailApiView.as_view(),name='sahip-detail'),
    
    path('turler/',api_views.KindListCreateAPIView.as_view(),name='turler-listesi'),
    path('tur/<int:pk>',api_views.KindDetailApiView.as_view(),name='tur-detail'),
    
    path('hayvanlar/',api_views.AnimalListCreateAPIView.as_view(),name='hayvanlar-listesi'),
    path('hayvan/<int:pk>',api_views.AnimalDetailApiView.as_view(),name='hayvan-detail')
]