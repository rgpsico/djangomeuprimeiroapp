
from django.contrib import admin
from django.urls import path
from app.views import home, form , create ,view ,Edit, update , delete , login ,logout,cadastro,addcart,deleteCard, pagar
from app.models import Carros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', cadastro, name="cadastro"),
    path('login/',login,name="login"),
    path('logout/',logout, name="logout"),

    path('pagar/', pagar, name="pagar"),
    path('addcart/', addcart, name="addcart"),
    path('DelCart/<int:pk>', deleteCard, name="DelCart"),
    path('', home , name="home"),
    path('form/', form, name="form"),
    path('create/',create, name="create"),
    path('view/<int:pk>', view, name="view"),
    path('edit/<int:pk>', Edit, name="edit"),
    path('update/<int:pk>', update, name="update"),
    path('delete/<int:pk>', delete, name="delete"),
]
