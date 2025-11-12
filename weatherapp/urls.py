from django.urls import path, include
from rest_framework.routers import DefaultRouter
from weatherapp import views

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'weather', views.WeatherDataViewSet, basename='weather')

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', views.dashboard, name='dashboard'),
]
