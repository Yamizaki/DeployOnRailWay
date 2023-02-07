from django.urls import path
from . import views

urlpatterns = [

    path('', views.solicitud, name="solicitud"),
    path('formulario/', views.contact_view, name="formulario"),
]