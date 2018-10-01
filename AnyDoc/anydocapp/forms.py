from django.contrib.auth.models import User
from django import forms
from .models import Radevou, Giatroi

def ex2(a):
    global ful
    ful = a
    print(a)

def ex1(a):
    global rad
    rad = a
    print(a)

def formes2(eee,ppp,fff):
    #metavlites p eftiaksa gia to search
    global radevus
    global giatroi
    global eidikotites
    global perioxes
    global tils
    global fullnames
    global amkas
    global e
    global f
    global t
    global p
    global a
    global r
    #metavlites p einai apo formes
    global eid
    global perio
    global ful
    global rad
    global t
    global d
    global ee
    global ff
    global pp
    global rr
    global aa
    global tt
    radevus = []
    giatroi = Giatroi.objects.all()
    eidikotites = []
    perioxes = []
    tils = []
    fullnames = []
    amkas = []
    for i in giatroi:
        rad = str(i.radevous)
        rarray = rad.split(",")
        for j in rarray:
            print(j)
            if(j == "") or (j==" "):
                continue
            radevus.append(j)
        eidik = str(i.eidikotita)
        eidikotites.append(eidik)
        peri = str(i.perioxi)
        perioxes.append(peri)
        til = i.til
        til = str(til)
        til = til.strip( '[Decimal(''),' )
        tils.append(til)
        full = str(i.fullname)
        fullnames.append(full)
        am = i.amka
        am = str(am)
        am = am.strip('[Decimal(''),')
        amkas.append(am)



    for i in giatroi:
        print(i.eidikotita)
        print(i.perioxi)
        print(eee)
        print(ppp)
        if i.eidikotita == eee and i.perioxi == ppp:
            e=eee
            p=ppp
            full = str(i.fullname)
            if full != "" and full != " ":
                print(full)
                fullnames.append(full)
                print(fullnames)
#
    radevus = []
    for i in giatroi:
        if i.fullname == fff:
            rad = str(i.radevous)
            rarray = rad.split(",")
            for j in rarray:
                print(j)
                if (j == "") or (j == " "):
                    continue
                radevus.append(j)
            r=radevus
    return r




def formes(eee,ppp):
    #metavlites p eftiaksa gia to search
    global radevus
    global giatroi
    global eidikotites
    global perioxes
    global tils
    global fullnames
    global amkas
    global e
    global f
    global t
    global p
    global a
    global r
    #metavlites p einai apo formes
    global eid
    global perio
    global ful
    global rad
    global t
    global d
    global ee
    global ff
    global pp
    global rr
    global aa
    global tt
    radevus = []
    giatroi = Giatroi.objects.all()
    eidikotites = []
    perioxes = []
    tils = []
    fullnames = []
    amkas = []
    for i in giatroi:
        rad = str(i.radevous)
        rarray = rad.split(",")
        for j in rarray:
            print(j)
            if(j == "") or (j==" "):
                continue
            radevus.append(j)
        eidik = str(i.eidikotita)
        eidikotites.append(eidik)
        peri = str(i.perioxi)
        perioxes.append(peri)
        til = i.til
        til = str(til)
        til = til.strip( '[Decimal(''),' )
        tils.append(til)
        full = str(i.fullname)
        fullnames.append(full)
        am = i.amka
        am = str(am)
        am = am.strip('[Decimal(''),')
        amkas.append(am)


    print(eidikotites)
    ee = dict((k, k) for k in eidikotites)
    ee = ee.items()
    ee = tuple(ee)
    print(ee)


    pp = dict((k, k) for k in perioxes)
    pp = pp.items()
    pp = tuple(pp)
    print(pp)


    # print(fullnames)
    # print("  names")
    # print(e)
    # print("  e")
    # print(i.eidikotita)
    # print("  ieidi")
    # print(p)
    # print("  p")
    # print(i.perioxi)
    # print("  iperi")


    for i in giatroi:
        print(i.eidikotita)
        print(i.perioxi)
        print(eee)
        print(ppp)
        if i.eidikotita == eee and i.perioxi == ppp:
            e=eee
            p=ppp
            full = str(i.fullname)
            if full != "" and full != " ":
                print(full)
                fullnames.append(full)
                print(fullnames)
#
    #radevus = []
    #for i in giatroi:
    #    if i.fullname == ful:
    #        rad = str(i.radevous)
    #        rarray = rad.split(",")
    #        for j in rarray:
    #            print(j)
    #            if (j == "") or (j == " "):
    #                continue
    #            radevus.append(j)


    ff = dict((k, k) for k in fullnames)
    ff = ff.items()
    ff = tuple(ff)
    print(ff)


    tt = dict((k, k) for k in tils)
    tt = tt.items()
    tt = tuple(tt)
    print(tt)


    aa = dict((k, k) for k in amkas)
    aa = aa.items()
    aa = tuple(aa)
    print(aa)

    rr = dict((k, k) for k in radevus)
    rr = rr.items()
    rr = tuple(rr)
    print(rr)


radevus = []
giatroi = Giatroi.objects.all()
eidikotites = []
perioxes = []
tils = []
fullnames = []
amkas = []
ee = []
ff = []
tt = []
pp = []
aa = []
rr = []
eid = ""
perio = ""
ful = ""
rad = ""
t = ""
d = ""
e = ""
f = ""
p = ""
a = ""
r = ""
formes("","")
class UserRegFrom(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.DecimalField(max_digits=11, decimal_places=0, min_value=10000000000,error_messages={'required': '11 Digitis for AMKA!'})

    class Meta:
        model = User
        fields = ['username', 'password']


class ResetPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['password']





class Ep(forms.Form):
    #formes()
    eidi = forms.ChoiceField(label="Specialties",
                                       widget=forms.Select(attrs={'class': 'form-control',
                                                                  'data-toggle': 'select'}),
                                       choices=ee, required=True)
    ##global e
    ##e = eidi
    ##formes()

    perioxi = forms.ChoiceField(label="Areas",
                             widget=forms.Select(attrs={'class': 'form-control',
                                                        'data-toggle': 'select'}),
                             choices=pp, required=True)
    #global p
    #p = perioxi
    #formes()


class Fu(forms.Form):
    formes(e,p)
    fn = forms.ChoiceField(label="Fullnames",
                             widget=forms.Select(attrs={'class': 'form-control',
                                                        'data-toggle': 'select'}),
                             choices=ff, required=True)
    #global f
    #f = fn
    #formes()




class Ra(forms.Form):
    #formes()
    ra = forms.ChoiceField(label="Dates",
                             widget=forms.Select(attrs={'class': 'form-control',
                                                        'data-toggle': 'select'}),
                             choices=rr, required=True)
    #global r
    #r = ra
    #formes()


class Rade(forms.ModelForm):
    class Meta:
        model = Radevou
        fields = ['title' ,'description' ]


#formes()
