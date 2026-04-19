from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('comment/delete/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('comment/like/<int:pk>/', views.like_comment, name='like_comment'),
    path('', views.product_list, name='product_list'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]