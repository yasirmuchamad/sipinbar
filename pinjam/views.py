from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def listBarang(request):
    barang = Barang.objects.all()

    context = {
        'title' : "Daftar Barang",
        'barangs' : barang,
    }

    return render(request, 'barang/list.html', context)

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

def listPinjam(request):
    pinjam = Pinjam.object.all()

    context = {
        'title' : "Daftar Terpinjam",
        'pinjams' : pinjam,
    }
    return render(request, 'pinjam/list.html', context)