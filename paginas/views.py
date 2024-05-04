from django.shortcuts import render
from categorias.models import EstadoDeConservacaoModels, CategoriaModels
from .models import HomeModels, QualidadesHomeModels
from django.views.generic import View
from carro.models import CarroModels


class HomeIndex(View):

    def get(self, *args, **kwargs):
        personalizacoes = HomeModels.objects.filter(
            publicado_home=True).order_by('-id').first()
        carros = CarroModels.objects.filter(
            publicado=True, destaque=True).order_by('-id')
        estados_de_conservacao = EstadoDeConservacaoModels.objects.all()        
        categorias = CategoriaModels.objects.all()
        qualidades = QualidadesHomeModels.objects.filter(
            publicado_qualidade=True)

        context = {
            'personalizacoes': personalizacoes,
            'carros': carros,
            'estados_de_conservacao': estados_de_conservacao,            
            'categorias': categorias,
            'qualidades': qualidades,
        }

        return render(self.request, 'home/index.html', context)
