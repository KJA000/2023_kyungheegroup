from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='products'),
 path('post/', views.post_product, name='product-post'),
 path('<int:product_id>/delete/', views.delete_product, name='product-delete'),
 path('products/<int:product_id>/', views.product_detail, name='product-detail'),
]
