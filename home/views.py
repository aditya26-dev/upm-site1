from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
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

    if request.method == 'POST':
            post = request.POST
            nama_file = post['nama_file']
            desc_file = post['desc_file']
            link_file = post['link_file']
            nama_folder = models.baruFolder.objects.get(id = post['nama_folder'])
            new_file = models.baruFile(
                nama_file = nama_file,
                desc_file = desc_file,
                link_file = link_file,
                nama_folder = nama_folder
            )
            new_file.save()

    return render(request, 'editForm.html', context)

def dashboardFolderForm(request):

    form = forms.inputFolderInfo()
    context = {
        'form': form,
    }

    if request.method == 'POST':
            post = request.POST
            nama_folder = post['nama_folder']
            desc_folder = post['desc_folder']
            baseFolder_nama = models.baseFolder.objects.get(id = post['baseFolder_nama'])
            prodi_name = models.listProdi.objects.get(id = post['prodi_name'])
            new_file = models.baruFolder(
                nama_folder = nama_folder,
                desc_folder = desc_folder,
                baseFolder_nama = baseFolder_nama,
                prodi_name = prodi_name
            )
            new_file.save()
    return render(request, 'editFolderForm.html', context)

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

def informasiUmum(request):

    folder = models.baruFolder.objects.filter(baseFolder_nama = 1)

    context = {
        'folder': folder,
    }
    return render(request, 'card01.html', context)

def akreditasiUmum(request):

    folder = models.baruFolder.objects.filter(baseFolder_nama = 7)

    context = {
        'folder': folder,
    }
    return render(request, 'card01.html', context)

def auditUmum(request):

    folder = models.baruFolder.objects.get(nama_folder = 'Audit Umum')
    files = models.baruFile.objects.filter(nama_folder = folder)

    context = {
        'files': files,
    }
    return render(request, 'list.html', context)

def auditProdi(request):

    folder = models.baruFolder.objects.filter(baseFolder_nama = 25)

    context = {
        'folder': folder,
    }
    return render(request, 'card01.html', context)

def akreditasiProdi(request):

    folder = models.baruFolder.objects.filter(baseFolder_nama = 19)

    context = {
        'folder': folder,
    }
    return render(request, 'card01.html', context)

def updateFile(request, file_id, folder_id):

    form = forms.inputFileInfo()
    files = models.baruFile.objects.get(id = file_id)

    form.nama_file = files.nama_file
    form.desc_file = files.desc_file
    form.link_file = files.link_file
    form.nama_folder = files.nama_folder

    context = {
        'form' : form,
    }

    return render(request, 'editForm.html', context)

def update_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(models.baruFile, id = id) 
  
    # pass the object as instance in form 
    form = forms.inputFileInfo(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return redirect('homepage') 
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "editForm.html", context)

def logout_user(request):
    logout(request)
    return redirect('homepage')

def delete_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(models.baruFile, id = id) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return redirect('homepage')
  
    return render(request, "delete_view.html", context) 

def update_folder_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(models.baruFolder, id = id) 
  
    # pass the object as instance in form 
    form = forms.inputFolderInfo(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return redirect('homepage')
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "editFolderForm.html", context)

def delete_folder_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(models.baruFolder, id = id) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return redirect('homepage')
  
    return render(request, "delete_view.html", context) 
