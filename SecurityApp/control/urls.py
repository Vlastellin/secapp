from django.urls import path

from . import views

urlpatterns = [
   path('qwe', views.login_index, name='login'),
   path('', views.index, name='table'),
   path('red', views.redirect_login, name='red')
]
