from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_akun, name='sosmed_home'),
]
