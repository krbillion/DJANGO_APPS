from django.urls import path
from . import views

app_name='posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('addPost', views.addPost, name='addPost'),
    path('details/<int:id>', views.details, name='details'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('signup', views.signup, name='signup'),
    path('search', views.search, name='search'),
    path('category', views.category, name='category'),
]
