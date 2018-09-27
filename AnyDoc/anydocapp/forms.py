from django.contrib.auth.models import User
from django import forms
from .models import Profile, Radevou, Giatroi

radevus = []
giatroi = Giatroi.objects.all()
eidikotites = []
perioxes = []
tils = []
fullnames = []
amkas = []
for i in giatroi:
    radevus.append(i.radevous)
    eidik = str(i.eidikotita)
    eidikotites.append(eidik)
    perioxes.append(i.perioxi)
    til = i.til
    til = str(til)
    til = til.strip( '[Decimal(''),' )
    tils.append(til)
    fullnames.append(i.fullname)
    amkas.append(i.amka)

print(eidikotites)



from .models import Profile, Radevou, Giatroi


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


class SetRadevou(forms.ModelForm):
    eidi = forms.MultipleChoiceField(
        required=True,
        widget=forms.MultipleChoiceField,
        choices=eidikotites,

    )
    class Meta:
        model = Radevou
        fields = ['title','eidi' , 'description', 'radevou',]