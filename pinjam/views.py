from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def is_admin(user):
    return user.is_staff

@login_required
def listBarang(request):
    barang = Barang.objects.all()

    context = {
        'title' : "Daftar Barang",
        'barangs' : barang,
    }

    return render(request, 'barang/list.html', context)

@login_required
def addBarang(request):
    form = BarangForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('pinjam:list_barang')

    context = {
        'title' : 'Tambah Barang',
        'forms'  : form,
    }
    return render(request, 'barang/create.html', context)

@login_required
def listPinjam(request):
    pinjam = Pinjam.objects.all()

    context = {
        'title' : "Daftar Terpinjam",
        'pinjams' : pinjam,
    }
    return render(request, 'pinjam/list.html', context)

@login_required
def addPinjam(request):
    form = PinjamForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pinjam = form.save(commit=False)
            pinjam.status = 'pending'
            pinjam.save()
            
            return redirect('pinjam:list_pinjam')

    context = {
        "title" : "Pinjam Barang",
        "forms" : form, 
    }
    return render(request, 'pinjam/create.html', context)

@user_passes_test(is_admin)
def approvePinjam(request, pk):
    pinjam = Pinjam.objects.get(pk=pk)

    if pinjam.status =='pending':
        barang = pinjam.barang
        if barang.stock > 0:
            barang.stock -= 1
            barang.save()

            pinjam.status = 'disetujui'
            pinjam.save()
        else:
            pinjam.status = 'ditolak'
            pinjam.save()

    return redirect('pinjam:list_pinjam')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pinjam:list_pinjam')
            else:
                # messages.error(request, 'Username atau password salah.')
                context = {
                    'form': form,
                    'error': 'Invalid Username or Password',
                    'title': 'Login',
                    'subtitle': 'Form',
                    # 'subsubtitle': 'System',
                }
                # messages.success(request, f'Selamat Datang , {user.username}')
                return render(request, 'pinjam/login.html', context)
        else:
            # print("Form errors:", form.errors)
            # messages.error(request, 'Username atau Password anda salah.')
            # messages.error(request, 'Form tidak valid. Coba lagi.')
            context = {
                'form': form,
                    'error': 'Invalid Username or Password',
                    'title': 'Login',
                    'subtitle': 'Form',
            }
            return render(request, 'pinjam/login.html', context)
    
    # Get request
    form = AuthenticationForm()
    context = {
        'title' : 'Login Form',
        'forms' : form,
    }
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('pinjam:login')