from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_accounts', views.show_accounts, name='show_accounts'),
]