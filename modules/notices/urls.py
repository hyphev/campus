from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('edit', views.edit, name='edit'),
    path('notice', views.notice, name='notice'),
]
