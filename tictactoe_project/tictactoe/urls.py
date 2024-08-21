from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('move/<int:position>/', views.make_move, name='make_move'),
    path('reset/', views.reset, name='reset'),
]
