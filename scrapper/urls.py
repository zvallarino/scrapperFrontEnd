from django.urls import path

from . import views

app_name = 'sonic'

urlpatterns = [
    path('', views.index, name='index'),
    path('facebook/', views.facebook, name='facebook'),
    path('twitter/', views.twitter, name='twitter'),
    path('reddit/', views.reddit, name='reddit'),
    path('data/', views.data_analytics, name='data'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('lists/', views.lists, name='lists'),
]