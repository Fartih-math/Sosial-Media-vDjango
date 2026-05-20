from django.contrib import admin
from .models import Instagram

@admin.register(Instagram)
class InstagramAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_depan', 'nama_belakang', 'username')
    search_fields = ('nama_depan', 'nama_belakang', 'username')