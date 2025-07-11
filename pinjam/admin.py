from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Barang)
class BarangAdmin(admin.ModelAdmin):
    list_display = ['nama_barang', 'stock']


@admin.register(Pinjam)
class PinjamAdmin(admin.ModelAdmin):
    list_display = ['karyawan', 'barang', 'tgl_pinjam', 'status']