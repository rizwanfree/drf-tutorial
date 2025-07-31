from django.urls import path

from api import views

urlpatterns = [
    path('products/', views.product_list),
    path('product/<int:pk>/', views.product_detail),

    path('orders/', views.order_list),
]