from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {
            'form':form
        }
        return render(request, 'users/register.html', context)

    def post(self, request):

        form = RegisterForm(data = request.POST)
        print("after valid")
        if form.is_valid():
            print("before validation")
            form.save()
            return redirect('users:login')
        else:
            return render(request, 'users/register.html', {'form':form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form':form})
    def post(self, request):

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "username or password error!")
            return render(request, 'users/login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')