from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='voc'),
    path('post_voc/',views.post_voc,name='post_voc')
]
