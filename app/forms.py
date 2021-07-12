from django.forms import ModelForm
from app.models import Carros , Produtos , Pedidos


class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['modelo','marca','ano']

class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['name','image','price']

