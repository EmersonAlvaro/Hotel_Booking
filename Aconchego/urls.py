from django.urls import path
from Aconchego import views

urlpatterns = [
    path('', views.aconchego, name="HomePage"),
    path('hotels/', views.hotels, name="hotels"),
    path('about/', views.about, name="about"),
    path('contacto/', views.contacto, name="contacto"),
    path('hotel_details<int:pk>/', views.hotels_details, name="hotel_details"),
    
]
