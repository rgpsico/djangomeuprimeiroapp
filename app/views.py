from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.db.models import Sum
from app.models import Carros, Produtos, Pedidos ,venda
from app.forms import CarrosForm, ProdutosForm
from django.db.models import Sum

from django.contrib.auth.models import User
# Create your views here.

def home(request):
    data = {}
    buscar =  request.GET.get('buscar')
    if buscar:
        data['db'] = Produtos.objects.filter(name__contains=buscar)
        data['pedido'] = Pedidos.objects.all()
    else:
        data['total'] = Pedidos.objects.all().aggregate(total=Sum('valor'))
        data['db'] = Produtos.objects.all()
        data['pedido'] = Pedidos.objects.all()

    return render(request, "index.html", data)


def addcart(request):
        item = request.POST['item']
        valor = request.POST['valor']
        quantidade = request.POST['quantidade']
        Pedidos.objects.create(item=item, valor=valor, quantidade=quantidade)
        return redirect('home')

def deleteCard(request, pk):
    data = {}
    db = Pedidos.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def pagar(request):
    total = request.POST['total']
    print(total)
    return redirect('home')



def form(request):
    data = {}
    data['form'] = CarrosForm
    return render(request, 'form.html', data)


def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)


def Edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'edit.html', data)


def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save
        return redirect('home')


def delete(request, pk):
    data = {}
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')


def cart(request):
    data = {}
    produtos = {}
    data['db'] = Carros.objects.all()
    data['produtos'] = Produtos.objects.all()
    data['total'] = Produtos.objects.aggregate(ValorTotal=Sum('price'))
    return render(request, "cart.html", data)


def DeleteProduto(request, pk):
    Produtos = Produtos.objects.get(pk=pk)
    Produtos.delete()
    return redirect('cart')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')


def cadastro(request):
    nome = request.POST.get('name')
    email = request.POST.get('email')
    senha = request.POST.get('senhaum')
    senha2 = request.POST.get('senhadois')

    if senha != senha2:
        print("senha nao pode ser diferentes")
    if User.objects.filter(username=nome).exists():
        print("usuario ja existe")

    if User.objects.filter(email=email).exists():
       print("usuario ja existe")

    User.objects.create_user(username=nome,email=email,password=senha)

    return render(request, 'cadastro.html')
