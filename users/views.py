from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .forms import UserProfileUpdateForm


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, password=password1, email=email)
                auth.login(request, user)
                return redirect('/')
            except IntegrityError:
                error_message = '이미 등록된 아이디입니다.'
                return render(request, 'users/signup.html', {'error_message': error_message})
        else:
            error_message = '비밀번호가 일치하지 않습니다.'
            return render(request, 'users/signup.html', {'error_message': error_message})

    return render(request, 'users/signup.html')

def mypage(request):
    context = {
        'active_page': 'mypage',
        'email': request.user.email,
        'username': request.user.username,
    }
    return render(request, 'users/mypage.html', context)


def check_username_availability(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        is_taken = User.objects.filter(username=username).exists()
        return JsonResponse({'is_taken': is_taken})

def update_profile(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('mypage')  
    else:
        form = UserProfileUpdateForm(instance=request.user)
    
    context = {
        'form': form,
        'active_page': 'mypage',
    }
    return render(request, 'users/profile_edit.html', context)  # Note the change in the template name

