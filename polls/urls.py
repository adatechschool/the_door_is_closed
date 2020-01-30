from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('red', views.redirect_site, name='redirect_site'),
]
