from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegFrom, ResetPasswordForm, Ra, Ep, Rade, Fu
from .models import Profile, Radevou, Giatroi

#radevus = []
#giatroi = Giatroi.objects.all()
#eidikotites = []
#perioxes = []
#tils = []
#fullnames = []
#amkas = []
#for i in giatroi:
#    radevus.append(i.radevous)
#    eidikotites.append(i.eidikotita)
#    perioxes.append(i.perioxi)
#    til = i.til
#    til = str(til)
#    til = til.strip( '[Decimal(''),' )
#    tils.append(til)
#    fullnames.append(i.fullname)
#    amkas.append(i.amka)

# Create your views here.
eid=""
perio=""
ful=""
rad=""

def handler400(request):
    return render(request, '400.html', status=400)


def handler403(request):
    return render(request, '403.html', status=403)


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)

def radevou(request):
    users = User.objects.all
    giatroi = Giatroi.objects.all
    if request.method == 'POST' and request.user.is_authenticated:
        form = Ep(request.POST)
        if form.is_valid():
            eid = form.cleaned_data.get('eidi')
            perio = form.cleaned_data.get('perioxi')
            print(eid)
            print(perio)
            return render(request, 'radevou2.html', {'form': form, 'users': users,})
            return redirect(radevou2(request, ei, peri))

        else:
            return render(request, 'radevou.html', { 'form': form, 'users':users})
    elif request.method == 'GET' and request.user.is_authenticated:
        form = Ep()
        return render(request, 'radevou2.html', {'form': form, 'users': users})
    else:

        return render(request, 'home.html',)


def radevou2(request):
    users = User.objects.all
    giatroi = Giatroi.objects.all
    if request.method == 'POST' and request.user.is_authenticated:
        form = Fu(request.POST)
        if form.is_valid():
            ful = form.cleaned_data.get('fn')

            print(ful)
            return render(request, 'radevou3.html', {'form': form, 'users': users,})
            return redirect(radevou3(request, full, ei, peri))
        else:
            return render(request, 'radevou2.html', { 'form': form, 'users':users})
    elif request.method == 'GET' and request.user.is_authenticated:
        form = Fu()
        return render(request, 'radevou2.html', {'form': form, 'users': users})
    else:

        return render(request, 'home.html',)


def radevou3(request):
    users = User.objects.all
    giatroi = Giatroi.objects.all
    if request.method == 'POST' and request.user.is_authenticated:
        form = Ra(request.POST)
        if form.is_valid():
            rad = form.cleaned_data.get('ra')

            print(rad)

            #print(e)
            return render(request, 'radevou4.html', {'form': form, 'users': users, })
        else:
            return render(request, 'radevou3.html', {'form': form, 'users': users})
    elif request.method == 'GET' and request.user.is_authenticated:
        form = Ra()
        return render(request, 'radevou3.html', {'form': form, 'users': users})
    else:

        return render(request, 'home.html',)


def radevou4(request):
    users = User.objects.all
    giatroi = Giatroi.objects.all
    if request.method == 'POST' and request.user.is_authenticated:
        form = Rade(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('tilte')
            description = form.cleaned_data.get('description')
            Radevou.title=title
            Radevou.description=description
            Radevou.radevou=rad
            Radevou.eidi=eid
            Radevou.peri=perio
            Radevou.fu=ful
            print(Radevou)
            Profile.radevous=Profile.radevous + " " + rad
            Profile.save()
            if rad in  Giatroi.radevous:
                Giatroi.radevous =  Giatroi.radevous.replace(rad, " ")
                Giatroi.radevous.save()


            form.save()


            #print(e)
            return render(request, 'radevus.html', { 'users': users})
        else:
            return render(request, 'radevou4.html', { 'form': form, 'users':users})
    elif request.method == 'GET' and request.user.is_authenticated:
        form = Rade()
        return render(request, 'radevou4.html', {'form': form, 'users':users})
    else:

        return render(request, 'home.html',)














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

def radevus(request):

    context = {
    }
    return render(request, 'radevus.html', context)


def contact(request):
    context = {


    }
    return render(request, 'contact.html', context)


