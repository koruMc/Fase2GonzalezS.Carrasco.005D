from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/', views.contacto, name='contact'),
    path('about/', views.about, name='about'),
    path('ciudad/<int:pk>', views.CiudadDetailView.as_view(), name='ciudad-detail'),
    path('destino/<str:pk>', views.DestinoDetailView.as_view(), name='destino-detail'),
]

urlpatterns += [
    path('ciudad/create/', views.ciudad_new,name='ciudad_create'),
    path('ciudad/<int:pk>/update/', views.ciudad_edit, name='ciudad_update'),
    path('ciudad/<int:pk>/delete/', views.CiudadDelete.as_view(), name='ciudad_delete'),
    path('destino/create/', views.destino_new,name='destino_create'),
    path('destino/<str:pk>/update/', views.destino_edit, name='destino_update'),
    path('destino/<str:pk>/delete/', views.DestinoDelete.as_view(), name='destino_delete'),
]