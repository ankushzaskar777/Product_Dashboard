
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [

    path('', views.home, name="home"),
    path('show/', views.show, name="show"),
    path('add/', views.add, name="add"),
    path('delete/<int:pid>',views.delete,name="delete"),
    path('edit/<int:pid>',views.edit,name="edit"),
    path('login/', views.login_view, name='login'),
    path('register/',views.register,name='register'),
    path('logoutu/', views.logout_view, name='logout'),
    path('search/', views.search_products, name='search'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('contact/', views.contact, name='contact')

  
]


