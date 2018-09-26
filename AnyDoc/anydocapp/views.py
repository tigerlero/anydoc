from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegFrom, ResetPasswordForm, UpdateRadevou, SetRadevou
from .models import Profile, Radevou, Giatroi


# Create your views here.

def handler400(request):
    return render(request, '400.html', status=400)


def handler403(request):
    return render(request, '403.html', status=403)


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)

def radevou(request):
    radevus = []
    giatroi = []
    giatroi = Giatroi.objects
    print(giatroi)





    return render(request, 'radevou.html')


def resetpass(request):
    if request.method == 'GET' and request.user.is_authenticated:
        form = ResetPasswordForm()
        return render(request, 'resetpass.html', {'form': form,})
    elif request.method == 'POST' and request.user.is_authenticated:
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_pwd = form.cleaned_data["password"]
            uname = request.user.username
            user = User.objects.get(username=uname)
            user.set_password(new_pwd)
            user.save()
            return render(request, 'home.html', )
        else:
            return render(request, 'resetpass.html', {'form': form,})
    else:
        return render(request, 'signin.html', )



def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', )
    elif request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return render(request, 'home.html',)
        else:
            error = 'Username or password are invalid. Please, try again.'
            return render(request, 'signin.html', {'error': error,})
    else:
        return render(request, 'home.html',)


def signup(request):
    if request.method == 'POST':

        form = UserRegFrom(request.POST)
        if form.is_valid():
            #email = form.cleaned_data["email"]
            uname = form.cleaned_data["username"]
            user = form.save(commit=False)
            pwd = form.cleaned_data["password"]
            user.set_password(pwd)
            user.save()
            user = authenticate(username=uname, password=pwd)
            profile = Profile(user_id=user.id)
            login(request, user)
            return render(request, 'home.html', )

        else:
            return render(request, 'signup.html', {'form': form})
    else:
        if request.method == 'GET':
            form = UserRegFrom()
            return render(request, 'signup.html', {'form': form,})




def signout(request):
    logout(request)
    return render(request, 'signin.html')


def home(request):
    context = {


    }
    return render(request, 'home.html', context)


def contact(request):
    context = {


    }
    return render(request, 'contact.html', context)


