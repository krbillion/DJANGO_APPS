from django.urls import path

from . import views

app_name='mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('cart', views.cart, name='cart'),
]
