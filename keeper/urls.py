from django.urls import path
from . import views

app_name = 'keeper'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('guards/', views.guards, name = 'guards'),
    path('residents/', views.residents, name = 'residents'),
    path('register_page/', views.register_page, name = 'returnRegisterPage'),
    path('find_page/', views.find_page, name = 'returnFindPage'),
]
