from django.shortcuts import render
from categorias.models import EstadoDeConservacaoModels, CategoriaModels
from .models import HomeModels, QualidadesHomeModels, SobreNosModels, FuncionarioModels
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


class SobreNosIndex(View):

    def get(self, *args, **kwargs):
        personalizacoes = SobreNosModels.objects.filter(
            publicado_sobre_nos=True).order_by('-id').first()
        funcionarios = FuncionarioModels.objects.filter(
            publicado=True).order_by('-id')
        estados_de_conservacao = EstadoDeConservacaoModels.objects.all()
        categorias = CategoriaModels.objects.all()

        context = {
            'personalizacoes': personalizacoes,
            'funcionarios': funcionarios,
            'estados_de_conservacao': estados_de_conservacao,
            'categorias': categorias,
        }

        return render(self.request, 'sobre_nos/index.html', context)
