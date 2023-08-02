from django.urls import path
from . import views
urlpatterns = [
 path('', views.mainpage,name="home"),
 path('company/', views.company),
]
