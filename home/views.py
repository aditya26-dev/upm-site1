from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from . import models, forms



# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    form = forms.CustomUserLogin()
    context = {
        'form': form,
    }

    if request.method == 'POST':
        post = request.POST
        email = post['email']
        password = post['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html', context)
    

def card1(request):
    return render(request, 'card.html')

def list1(request):
    files = models.InformasiFile.objects.all()

    context = {
        'files': files,
    }
    return render(request, 'list.html', context)



