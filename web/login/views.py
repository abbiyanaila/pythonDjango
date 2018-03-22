# redirect apa ya
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from login.forms import *

# Create your views here.
# ini adalah class yang akan di eksekusi pada url, pemanggilannya harus sesuai dengan nama class

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('room:list')
        else:
            templateName = 'login/index.html' #pemanggilan ke list.html
            form = LoginForm(request.POST or None)
            data = {
                'form' : form,
                'error': False,
            }
            return render(request, templateName, data)


class DoLogin(View):
    def post(self, request):
        templateName = 'login/index.html' #pemanggilan ke list.html
        form = LoginForm(request.POST or None)
        auth = 'None'
        if form.is_valid():
            user = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            auth = authenticate(username=user, password=passwd)
            if auth is not None:
                login(request, auth)
                return redirect('room:list')   
                

        data = {
            'form' : form,
            'error': True,
            'auth': auth,
        }
        return render(request, templateName, data)
                


class DoLogout(View):
    def get(self, request):
        logout(request)
        return redirect('login:view')