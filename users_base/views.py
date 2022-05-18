from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def register(request):

    form_user = UserForm(request.POST or None)
    
    if form_user.is_valid():
        user = form_user.save()
        
        if 'profile_pic' in request.FILES:
            user.profile_pic = request.FILES['profile_pic']

        user.save()
        login(request,user)
        messages.success(request,'Register successful')

        return redirect('register')
    
    context = {
        'form_user':form_user,
    }

    return render(request, 'users_base/register.html', context)

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        # username = form.cleaned_data.get("username")
        # password = form.cleaned_data.get("password")

        # user = authenticate(username=username, password=password)
        user = form.get_user()
        if user:
            messages.success(request, "Login Successfull")
            login(request,user)
            return redirect('login')

    return render(request, 'users_base/user_login.html', {"form":form})

def user_logout(request):
    messages.success(request,'You logged out!')
    logout(request)
    return redirect('login')