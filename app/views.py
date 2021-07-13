from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from app.models import Carros, Produtos, Pedidos ,venda , itens_vendido
from app.forms import CarrosForm, ProdutosForm
from django.db.models import Sum
from django.contrib import auth , messages
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    data = {}
    buscar = request.GET.get('buscar')
    if request.user.is_authenticated:
        id = request.user.id
        pedidos = Pedidos.objects.order_by('id').filter(Pessoa=id)
        data['total'] = Pedidos.objects.filter(Pessoa_id=id).aggregate(total=Sum('valor'))
        data['pedido'] = pedidos
        data['db'] = Produtos.objects.all()
        return render(request, "index.html", data)
    if buscar:
        data['db'] = Produtos.objects.filter(name__contains=buscar)
        return render(request, "index.html", data)
    else:
        data['db'] = Produtos.objects.all()



        return render(request, "index.html", data)


def addcart(request):
    item = request.POST['item']
    valor = request.POST['valor']
    quantidade = request.POST['quantidade']

    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)
        Pedidos.objects.create(Pessoa=user,item=item, valor=valor, quantidade=quantidade)
        messages.success(request, 'O Produto '+item+' adicionado no seu carrinho')
        return redirect('home')
    else:
        request.session['carrinho'] = {'item':item, 'valor':valor, 'quantidade':quantidade}
        carrinho = request.session['carrinho']

        return redirect('home')

def deleteCard(request, pk):
    data = {}
    db = Pedidos.objects.get(pk=pk)
    db.delete()
    messages.error(request, 'O Produto ' + db.item + ' foi exluido com sucesso')
    return redirect('home')

def cadastrarProd(request):
    return render(request, "addprod.html")

def insertProd(request):
    name = request.POST['name']
    image = request.POST['image']
    price = request.POST['price']

    user = get_object_or_404(User, pk=request.user.id)
    Produtos.objects.create(Pessoa=user,name=name,image=image,price=price)
    messages.success(request, 'Produto cadastrado com Sucesso')
    return render(request, "addprod.html")

def listarprodutos(request):
    data = {}
    id = request.user.id
    buscar = request.GET.get('buscar')
    if buscar:
        data['db'] = Produtos.objects.filter(name__contains=buscar)
    if id:
        data['db'] = Produtos.objects.filter(Pessoa=id)
    else:
        data['db'] = Produtos.objects.all()
    return render(request, "listProd.html", data)

def deleteProd(request, pk):
    data = {}
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return redirect('listarprodutos')



def pagar(request):
    id = request.user.id
    total = request.POST['total']
    if request.user.is_authenticated:
        data = {}
        teste = data['db'] = Pedidos.objects.filter(Pessoa=id)
        id_venda = venda.objects.create(total=total)
    for variacao in teste:
        itens_vendido.objects.create(Pessoa_id=id,item=variacao.item,valor=variacao.valor,quantidade=variacao.quantidade,venda_id=id_venda.id)
        Pedidos.objects.filter(Pessoa_id=id).delete()
    else:
        return redirect('home')

def todasasvendas(request):
    data = {}
    id = request.user.id
    buscar = request.GET.get('buscar')
    if buscar:
        data['db'] = venda.objects.all()
    if id:
        data['db'] = venda.objects.all()
    else:
        data['db'] = venda.objects.all()
    return render(request, "vendas/vendas.html", data)

def detalhesvedas(request,pk):
      data = {}
      data['db']  = itens_vendido.objects.filter(venda_id=pk)
      data['total'] = itens_vendido.objects.filter(venda_id=pk).aggregate(total=Sum('valor'))
      return render(request, "vendas/detalhes.html", data)

def checkout(request):
    data = {}
    id = request.user.id

    if request.user.is_authenticated:
        pedidos = Pedidos.objects.order_by('id').filter(Pessoa=id)
    else:
        messages.error(request, 'E preciso esta logado para fazer checkout')
        return redirect(home)
    if pedidos:
        data['total'] = Pedidos.objects.all().aggregate(total=Sum('valor'))
        data['pedido'] = pedidos
        return render(request, "vendas/checkout.html", data)
    else:
        messages.error(request, 'E preciso ter produto para fazer o checkout')
        return redirect(home)


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

def logar(request):
     if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "":
            messages.error(request, 'email  vazio ou invalido')


        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username',flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.error(request, 'login realizado com successo')
                return redirect('listarprodutos')
            else:
                messages.error(request, 'Não logouo')
                return redirect('login')



def logout(request):
    auth.logout(request)
    return redirect('home')

def cadastro(request):
    return render(request, 'cadastro.html')

def insertuser(request):
    if request.method == 'POST':
        nome = request.POST.get('name')
        email = request.POST.get('email')
        senha = request.POST.get('senhaum')
        senha2 = request.POST.get('senhadois')

    if senha != senha2:
       messages.error(request,'As senhas não são iguais')
       return redirect('../cadastro')
    if User.objects.filter(username=nome).exists():
       messages.error(request, 'usuario ja existe')
       return redirect('../cadastro')

    if User.objects.filter(email=email).exists():
       messages.error(request, 'E-mail ja existe')
       return redirect('../cadastro')

    user = User.objects.create_user(username=nome, email=email, password=senha)
    user.save()
    messages.success(request, 'usuario cadastrado com sucesso')
    return render(request, 'cadastro.html')
