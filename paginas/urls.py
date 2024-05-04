from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeIndex.as_view(), name='home'),
    path('sobre-nos/', views.SobreNosIndex.as_view(), name='sobre-nos'),
    path('estoque/', views.EstoqueIndex.as_view(), name='estoque'),
    path('estoque/carro/<int:pk>', views.CarroDetalhes.as_view(), name='carro_detalhes'),
    path('estoque/busca/', views.CarroBusca.as_view(), name='carro_busca'),
    path('estoque/filtro/', views.CarroFiltro.as_view(), name='carro_filtro'),
]
