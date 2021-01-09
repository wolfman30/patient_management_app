from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_patient, name='add'),
    path('fetch/', views.fetch_patient, name='fetch'),
]
