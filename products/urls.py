from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='products'),
 path('post/', views.post_product, name='product-post'),
 path('<int:product_id>/delete/', views.delete_product, name='product-delete'),
 path('<int:product_id>/', views.product_detail, name='product-detail'),
 path('comment/create/<int:product_id>/', views.comment_create, name='comment_create'),
 path('comment/update/<int:comment_id>/', views.comment_update,name='comment_update'),
 path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]
