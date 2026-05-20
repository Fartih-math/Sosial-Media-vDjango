from django.shortcuts import redirect

def index(request):
    return redirect('sosmed:sosmed_home')
