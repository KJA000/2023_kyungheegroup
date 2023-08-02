from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as custom_views


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signup/', custom_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='../../'), name='logout'),
    path('mypage/', custom_views.mypage, name='mypage'),
    path('check_username/', custom_views.check_username_availability, name='check_username_availability'),
]
