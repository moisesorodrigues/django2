from django import forms

from tempus_dominus.widgets import DatePicker

from datetime import datetime

from aplicativoairlines.tipos_classe import tipos_de_classe

from aplicativoairlines.validation import *

from aplicativoairlines.models import Passagem, ClasseViagem, Pessoa

""" class PesquisaPassagensForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    tipo_classe = forms.ChoiceField(label='Tipo de classe do vôo', choices=tipos_de_classe)
    info = forms.CharField(
        label='Informações extras',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='E-mail', max_length=150) """

class PesquisaPassagensForms(forms.ModelForm):

    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    
    class Meta:
        model = Passagem
        #fields = ['origem', 'destino', 'data_ida']
        fields = '__all__'
        labels = {'data_ida': 'Data de ida', 'data_volta': 'Data de volta', 
                    'data_pesquisa': 'Data de pesquisa', 'classe_viagem': 'Classe da viagem', 
                    'informacoes': 'Informações'}
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker()
        }

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        erros = {}
        
        validar_valor_alfa('origem', origem, erros)
        validar_valor_alfa('destino', destino, erros)
        validar_origem_destino_iguais(origem, destino, erros)
        validar_periodo_viagem(data_ida, data_volta, data_pesquisa, erros)

        if erros is not None:
            for erro in erros:
                mensagens_erro = erros[erro]
                self.add_error(erro, mensagens_erro)
        
        return self.cleaned_data

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        #fields = ['email']
        exclude = ['nome']