from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from . import models, forms



# Create your views here.
def page_login(request):
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

def dashboardForm(request):

    form = forms.inputFileInfo()
    context = {
        'form': form,
    }

    if form.is_valid(): 
        form.save() 

    if request.method == 'POST':
        post = request.POST
        nama_file = post['nama_file']
        desc_file = post['desc_file']
        link_file = post['link_file']

    return render(request, 'editForm.html', context)

def dashboardFile(request):
    return render(request, 'FileList.html')

def dashboardFolder(request):
    return render(request, 'FolderList.html')

def homepage(request):
    if request.user.is_authenticated == False:
        return redirect('login')

    if request.user.prodi == 'DBT':
        context = {
            'Prodi' : 'Digital Business Technology'
        }
        return render(request, 'card.html', context)
    
    elif request.user.prodi == 'FBT':
        context = {
            'Prodi' : 'Food Business Technology'
        }
        return render(request, 'card.html', context)
    
    elif request.user.prodi == 'BM':
        context = {
            'Prodi' : 'Business Mathematics'
        }
        return render(request, 'card.html', context)

    elif request.user.prodi == 'PDE':
        context = {
            'Prodi' : 'Product Design Engineering'
        }
        return render(request, 'card.html', context)

    elif request.user.prodi == 'REE':
        context = {
            'Prodi' : 'Renewable Energy Engineering'
        }
        return render(request, 'card.html', context)

    elif request.user.prodi == 'CSE':
        context = {
            'Prodi' : 'Computer System Engineering'
        }
        return render(request, 'card.html', context)

