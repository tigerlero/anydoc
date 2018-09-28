from django.contrib.auth.models import User
from django import forms
from .models import Profile, Radevou, Giatroi, Eid

radevus = []
giatroi = Giatroi.objects.all()
eidikotites = []
perioxes = []
tils = []
fullnames = []
amkas = []
for i in giatroi:
    rad = str(i.radevous)
    radevus.append(rad)
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


class UserRegFrom(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.DecimalField(max_digits=11, decimal_places=0, min_value=10000000000)

    class Meta:
        model = User
        fields = ['username', 'password']


class ResetPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['password']

class UpdateRadevou(forms.ModelForm):
    class Meta:
        model = Radevou
        fields = ['title', 'description', 'radevou', 'perioxi']


e = dict((k,k) for k in eidikotites)
e = e.items()
e=tuple(e)
print(e)

f = dict((k,k) for k in fullnames)
f = f.items()
f=tuple(f)
print(f)

t = dict((k,k) for k in tils)
t = t.items()
t=tuple(t)
print(t)

p = dict((k,k) for k in perioxes)
p = p.items()
p=tuple(p)
print(p)

a = dict((k,k) for k in amkas)
a = a.items()
a=tuple(a)
print(a)

r = dict((k,k) for k in radevus)
r = r.items()
r=tuple(r)
print(r)


class Eidi(forms.ModelForm):
    #eidi = forms.MultipleChoiceField(
    #    required=False,
    #    widget=forms.CheckboxSelectMultiple,
    #    choices=FAVORITE_COLORS_CHOICES,
    #)
    eidi = forms.ChoiceField(label="Specialties",
                                       widget=forms.Select(attrs={'class': 'form-control',
                                                                  'data-toggle': 'select'}),
                                       choices=e, required=True)

    perioxi = forms.ChoiceField(label="Areas",
                             widget=forms.Select(attrs={'class': 'form-control',
                                                        'data-toggle': 'select'}),
                             choices=p, required=True)

    fn = forms.ChoiceField(label="Fullnames",
                             widget=forms.Select(attrs={'class': 'form-control',
                                                        'data-toggle': 'select'}),
                             choices=f, required=True)

    ra = forms.ChoiceField(label="Dates",
                             widget=forms.Select(attrs={'class': 'form-control',
                                                        'data-toggle': 'select'}),
                             choices=r, required=True)
    class Meta:
        model = Eid
        fields = ['eidi', 'perioxi', 'fn', 'ra']


