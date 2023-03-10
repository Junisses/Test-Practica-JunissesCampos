from django.urls import path
from .views import CustomerView, Prueba, EtapaView, ProspectoView, UsuarioView
from . import views

urlpatterns = [
    #CLIENTES
    path('clientes/', CustomerView.as_view(), name='clientes'),
    path('clientes/<int:id>', CustomerView.as_view(), name='clientes_proceso'),

    #ESTADO
    path('estados/', Prueba.as_view(), name='estados'),
    path('estados/<int:id>', Prueba.as_view(), name='estados_proceso'),

    #ETAPA
    path('etapas/', EtapaView.as_view(), name='etapas'),
    path('etapas/<int:id>', EtapaView.as_view(), name='etapas_proceso'),

    #PROSPECTO
    path('prospectos/', ProspectoView.as_view(), name='prospectos'),
    path('prospectos/<int:id>', ProspectoView.as_view(), name='prospectos_proceso'),

    #USUARIO
    path('usuarios/', UsuarioView.as_view(), name='usuarios'),
    path('usuarios/<int:id>', UsuarioView.as_view(), name='usuarios_proceso')
]
