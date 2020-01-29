from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lmao', views.print_submit, name='print_submit'),
]
