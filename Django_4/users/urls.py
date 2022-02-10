from django.contrib import admin
from django.urls import path
from .views import *
app_name="account"

urlpatterns = [
    path('login/',login_wiew,name="login" ),
    path('register/',register_view,name="register" ),
    path('logout/',logout_view,name="logout" ),
    # path('',home_wiev ,name="index_home"),
    # path('<str:slug>/delete/',home_delete ,name="delete"),
    # path('creat/',home_creat ,name="creat"),
    # path('<str:slug>/update/',home_update ,name="update"),
    # path('<str:slug>/list/',home_list ,name="detail"),

]
