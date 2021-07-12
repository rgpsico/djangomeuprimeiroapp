from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Categoria
from .models import Produtos


admin.site.register(Categoria)
admin.site.register(Produtos)
