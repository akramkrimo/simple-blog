from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model, login, authenticate, logout
# Create your views here.

User = get_user_model()

def register_view(request):
    if request.user.is_authenticated:
        return redirect('myblog:list')

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        birthdate = form.cleaned_data['birthdate']
        User.objects.create_user(
            username=username,
            password=password,
            email=email,
            birthdate=birthdate
        )
        return redirect('myblog:list')
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('myblog:list')

    form = LoginForm(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data['password']
        username = form.cleaned_data['username']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('myblog:list')
    return render(request, 'accounts/login.html', {'form': form})

def lougout_view(request):
    logout(request)
    return redirect('accounts:login')