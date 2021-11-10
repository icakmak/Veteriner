from django.urls import path
from VetApps.Apps import views as api_views

urlpatterns = [
    path('sahipler/',api_views.CustomerListCreateAPIView.as_view(),name='sahipler-listesi'),
    path('sahipler/<int:pk>',api_views.CustomerDetailApiView.as_view(),name='sahipler-detail'),
    
    path('turler/',api_views.KindListCreateAPIView.as_view(),name='turler-listesi'),
    path('turler/<int:pk>',api_views.KindDetailApiView.as_view(),name='turler-detail'),
    
    path('hayvanlar/',api_views.AnimalListCreateAPIView.as_view(),name='hayvanlar-listesi'),
    path('hayvanlar/<int:pk>',api_views.AnimalDetailApiView.as_view(),name='hayvanlar-detail')
]