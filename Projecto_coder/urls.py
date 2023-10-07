from django.urls import path, include
from AppCoder import views

urlpatterns = [
    path('', include('AppCoder.urls')),

    
]
