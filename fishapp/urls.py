from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:fish_id>/', views.details, name='details'),
    path('add/', views.add, name='add'),
    path('order/', views.order, name='order'),
    path('order/success', views.order_placed, name='order_placed'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
]
