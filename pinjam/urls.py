from django.urls import path
from . import views

app_name = 'pinjam'
urlpatterns = [
    path('barang', views.listBarang, name='list_barang'),
    path('barang/create', views.addBarang, name='add_barang'),
]