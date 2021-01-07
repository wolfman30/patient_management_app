from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('commoninfo/add/', views.add_patient, name='add-patient')
]