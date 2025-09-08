from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name=""),
    #path('store', views.store, name="store"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
]
