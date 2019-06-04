# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from laudosMedvet.models import RequisicaoLaudoModel
from laudosMedvet.models import LaudoModel


def consulta_requisicao(request):
    por_proprietario = request.GET.get('por_proprietario', None)
    por_animal = request.GET.get('por_animal', None)
    por_tipo = request.GET.get('por_tipo', None)

    if por_animal is not None:
        requisicoes = RequisicaoLaudoModel.objects.filter(cod_animail__nome__icontains=por_animal)
    elif por_proprietario is not None:
        requisicoes = RequisicaoLaudoModel.objects.filter(cod_animail__proprietario__nome_proprietario__icontains=por_proprietario)
    elif por_tipo is not None:
        requisicoes = RequisicaoLaudoModel.objects.filter(tipo_de_laudo__tipo_laudo__icontains=por_tipo)
    else:
        requisicoes = RequisicaoLaudoModel.objects.all()
    return render(request, 'consultas/por_requisição.html', {'requisicoes':requisicoes})


def consulta_laudo(request):
    por_proprietario = request.GET.get('por_proprietario', None)
    por_animal = request.GET.get('por_animal', None)
    por_tipo = request.GET.get('por_tipo', None)

    if por_animal is not None:
        laudos = LaudoModel.objects.filter(id_requisicao__cod_animail__nome__icontains=por_animal)
    elif por_proprietario is not None:
        laudos = LaudoModel.objects.filter(id_requisicao__cod_animail__proprietario__nome_proprietario__icontains=por_proprietario)
    elif por_tipo is not None:
        laudos = LaudoModel.objects.filter(id_requisicao__tipo_de_laudo__tipo_laudo__icontains=por_tipo)
    else:
        laudos = LaudoModel.objects.all()
    return render(request, 'consultas/por_laudo.html', {'laudos': laudos})