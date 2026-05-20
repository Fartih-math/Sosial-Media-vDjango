from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import AkunForm

# READ
def list_akun(request):
    semua_akun = User.objects.all()
    return render(request, 'list.html', {
        'semua_akun': semua_akun,
        'page_title': 'Daftar Akun'
    })

# CREATE
def create_akun(request):
    if request.method == 'POST':
        akun_form = AkunForm(request.POST)
        if akun_form.is_valid():
            akun_form.save()
            return redirect('sosmed:sosmed_home')
    else:
        akun_form = AkunForm()

    return render(request, 'create.html', {
        'akun_form': akun_form,
        'page_title': 'Tambah Akun Baru'
    })

# DELETE
def delete_akun(request, pk):
    akun = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        akun.delete()
        return redirect('sosmed:sosmed_home')
    return render(request, 'confirm_delete.html', {'akun': akun})

# UPDATE
def update_akun(request, pk):
    akun = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if first_name and last_name:
            akun.first_name = first_name
            akun.last_name = last_name
            akun.save()
            return redirect('sosmed:sosmed_home')

    return render(request, 'update.html', {
        'akun': akun,
        'page_title': 'Ubah Nama Akun'
    })
