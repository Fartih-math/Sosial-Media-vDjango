from django.shortcuts import render
from .models import UserPost

def list_akun(request):
    semua_akun = UserPost.objects.all()
    return render(request, 'list.html', {'semua_akun': semua_akun})
