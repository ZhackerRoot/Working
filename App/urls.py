from django.urls import path
from . import views

                

urlpatterns = [
   path('', views.login, name='login'),
   path('home/', views.home, name='home'),
   path('members', views.members, name='members'),
   path('about', views.about, name='about')

]