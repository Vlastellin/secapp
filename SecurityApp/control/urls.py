from django.urls import path

from . import views

urlpatterns = [
   path('', views.login_index, name='login'),
   path('table', views.index, name='table'),
   path('red', views.redirect_login, name='red')
]
