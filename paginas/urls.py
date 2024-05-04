from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeIndex.as_view(), name='home'),
    path('sobre-nos/', views.SobreNosIndex.as_view(), name='sobre-nos'),
]
