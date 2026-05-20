from django.urls import path
from . import views

app_name = 'sosmed'

urlpatterns = [
    path('', views.list_akun, name='sosmed_home'),
    path('create/', views.create_akun, name='create'),
    path('delete/<int:pk>/', views.delete_akun, name='delete'),
    path('update/<int:pk>/', views.update_akun, name='update'),
]
