from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('comment/delete/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('comment/like/<int:pk>/', views.like_comment, name='like_comment'),
]