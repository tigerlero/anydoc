from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegFrom, ResetPasswordForm, Ra, Ep, Rade, Fu, formes,formes2,formes3
from .models import Profile, Radevou, Giatroi
from datetime import datetime
import datetime
from django.utils import timezone
from datetime import timedelta
from dateutil import parser
def week_range(date):
    """Find the first/last day of the week for the given day.
    Assuming weeks start on Sunday and end on Saturday.

    Returns a tuple of ``(start_date, end_date)``.

    """
    # isocalendar calculates the year, week of the year, and day of the week.
    # dow is Mon = 1, Sat = 6, Sun = 7
    year, week, dow = date.isocalendar()

    # Find the first day of the week.
    if dow == 7:
        # Since we want to start with Sunday, let's test for that condition.
        start_date = date
    else:
        # Otherwise, subtract `dow` number days to get the first day
        start_date = date - timedelta(dow)

    # Now, add 6 for the last day of the week (i.e., count up to Saturday)
    end_date = start_date + timedelta(6)

    return (start_date, end_date)

eid = ""
perio=""
ful=""
rad = ""
t=""
d=""
til =""

def ex3(a,b):
    global eid
    global perio
    eid = a
    perio = b
    print(a)
    print(b)

def ex2(a):
    global ful
    ful = a
    print(a)

def ex1(a):
    global rad
    rad = a
    print(a)

def ex4():
    global eid
    global perio
    global ful
    global rad
    rad = ""
    ful = ""
    eid = ""
    perio = ""
#def epistrofi():
#    global eid
#    global perio
#    global ful
#    global rad
#    a = []
#    a.append(eid)
#    a.append(perio)
#    a.append(ful)
#    a.append(rad)
#    return a


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
            ex3(eid,perio)

            formes(eid,perio)
            return HttpResponseRedirect(reverse('radevou2') )
            #return render(request, 'radevou2.html', {'users':users})
        else:
            return render(request, 'radevou.html', { 'form': form, 'users':users})
    elif request.method == 'GET' and request.user.is_authenticated:
        form = Ep()
        return render(request, 'radevou.html', {'form': form, 'users': users})
    else:

        return render(request, 'home.html',)


def radevou2(request):
    formes(eid, perio)
    global rad

    users = User.objects.all
    giatroi = Giatroi.objects.all
    if request.method == 'POST' and request.user.is_authenticated:
        formes(eid, perio)
        form = Fu(request.POST)
        if form.is_valid():
            formes(eid, perio)
            ful = form.cleaned_data.get('fn')
            print(eid)
            print(perio)
            print(ful)
            ex2(ful)
            rad = formes2(eid, perio,ful)
            print("rad")

            return HttpResponseRedirect(reverse('radevou3'))
        else:
            formes(eid, perio)
            return render(request, 'radevou2.html', {'form': form, 'users': users,'eid':eid, 'perio':perio,'giatroi':giatroi,'rad':rad})
    elif request.method == 'GET' and request.user.is_authenticated:
        formes(eid, perio)
        form = Fu()

        return render(request, 'radevou2.html', {'form': form, 'users': users,'eid':eid, 'perio':perio,'giatroi':giatroi,'rad':rad})
    else:

        return render(request, 'home.html',)


def radevou3(request):
    global rad
    rad = formes2(eid, perio, ful)
    print("rad")
    print(rad)
    users = User.objects.all
    giatroi = Giatroi.objects.all
    if request.method == 'POST' and request.user.is_authenticated:
        form = Ra(request.POST)
        if form.is_valid():
            rad = form.cleaned_data.get('ra')
            print(rad)
            ex1(rad)
            #print(e)

            return HttpResponseRedirect(reverse('radevou4'))
        else:
            return render(request, 'radevou3.html', {'form': form, 'users': users,'rad' : rad,'ful':ful})
    elif request.method == 'GET' and request.user.is_authenticated:
        formes2(eid, perio, rad)
        form = Ra()
        return render(request, 'radevou3.html', {'form': form, 'users': users,'rad' :rad,'ful':ful})
    else:

        return render(request, 'home.html',)


def radevou4(request):

    users = User.objects.all
    giatroi = Giatroi.objects.all
    if request.method == 'POST' and request.user.is_authenticated:
        form = Rade(request.POST)
        if form.is_valid():
            global eid
            global perio
            global ful
            global rad
            global t
            global d
            global til
            til = formes3(eid, perio, ful)
            #til = Decimal(til)
            formes(eid, perio)
            t = form.cleaned_data.get('title')
            d = form.cleaned_data.get('description')
            user = request.user
            p = user.profile
            r = user.radevou_set.create(title=t, description=d, radevou=rad, eidi=eid, peri=perio, fu= ful,til=til)
            raaa = str(p.radevous) + " " + rad
            p.radevous=raaa
            p.save()
            g = Giatroi.objects.get(fullname=ful)
            g.radevous =  g.radevous.replace(r.radevou, "")
            g.save()
            ex4()
            formes(eid, perio)
            return HttpResponseRedirect(reverse('radevus'))
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
            profile.save()

            login(request, user)
            return render(request, 'home.html', )

        else:
            return render(request, 'signup.html', {'form': form})
    else:
        if request.method == 'GET':
            form = UserRegFrom()
            return render(request, 'signup.html', {'form': form,})




def signout(request):
    user = request.user
    print(user)
    return HttpResponseRedirect(reverse('signin'))

def home(request):

    return render(request, 'home.html')

def radevus(request):
    user = request.user
    print(user)
    r = user.radevou_set.all()
    dates = []
    for i in r:
        dates.append(i.radevou)
    now = timezone.now()
    now_string = now.strftime('%Y.%d.%m %H:%M')

    date_format = '%Y.%d.%m %H:%M'
    d = datetime.datetime(2018,10,1)
    print(d)
    week = week_range(d)
    print(week)

    years=[]
    days=[]
    month=[]
    datetimes = []
    hours=[]
    minutes=[]
    j=0

    weeks=[]
    for i in dates:

        years.append(i[:4])
        print(years)
        month.append(i[5:7])
        print(month)
        days.append(i[8:10])
        print(days)
        hours.append(i[11:13])
        print(hours)
        minutes.append(i[14:16])
        print(minutes)

        datetimes.append(datetime.datetime(year=int(years[j]), month=int(month[j]), day=int(days[j])))
        print(datetimes[j])



        j = j + 1
    today = datetime.datetime.today()
    last_monday = today - datetime.timedelta(days=today.weekday())
    print(last_monday)
    monday = today + datetime.timedelta(days=-today.weekday(), weeks=1)
    for k in range(51):
        print(k)
        next_monday = today + datetime.timedelta(days=-today.weekday(), weeks=k)

        for i in datetimes:
            if i < next_monday:
                weeks.append(datetimes)
    print(weeks)

            #weeks[k] =
    #Radevou.objects.filter(date_joined__range=week)

    print(now_string)
    for i in r:
        dates.append(i.radevou)





    return render(request, 'radevus.html', {'r':r,'user':user})

def contact(request):

    return render(request, 'contact.html')


