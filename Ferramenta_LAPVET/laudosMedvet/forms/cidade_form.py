from django.forms import ModelForm

from laudosMedvet.models import CidadeModel

class CidadeForm(ModelForm):
    class Meta():
        model = CidadeModel
        fields = ['id_regiao_estado', 'nome_cidade']