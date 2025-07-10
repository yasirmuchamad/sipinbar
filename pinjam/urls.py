from django.urls import path
from . import views

app_name = 'pinjam'
urlpatterns = [
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),

    path('barang', views.listBarang, name='list_barang'),
    path('barang/create', views.addBarang, name='add_barang'),

    path('pinjam', views.listPinjam, name='list_pinjam'),
    path('pinjam/create', views.addPinjam, name='add_pinjam'),
    path('pinjam/approve/<int:pk>/', views.approvePinjam, name='approve_pinjam'),
    path('pinjam/return/<int:pk>/', views.returnPinjam, name='return_pinjam')
]