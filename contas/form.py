from django.forms import ModelForm
from contas.models import Transacao

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao #Modelo que vou querer usar no CRUD
        fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria'] #Campos que vou querer do meu
