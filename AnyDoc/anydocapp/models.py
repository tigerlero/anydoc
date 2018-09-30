from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    radevous = models.TextField(max_length=3001)
    def __str__(self):
        return self.user.username


class Radevou(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=46)
    description = models.TextField(max_length=3001)
    eidi = models.CharField(max_length=80, default="")
    peri = models.CharField(max_length=80, default="")
    fu = models.CharField(max_length=50, default="")
    radevou = models.TextField(default=None, blank=False, null=False, primary_key = True)

    def __str__(self):
        return self.user.username


class Giatroi(models.Model):
    fullname = models.CharField(max_length=50)
    amka = models.DecimalField(max_digits=11, decimal_places=0, primary_key=True)
    eidikotita = models.CharField(max_length=50)
    til = models.DecimalField(max_digits=10, decimal_places=0)
    perioxi = models.CharField(max_length=50)
    radevous = models.TextField(max_length=3001)

    def __str__(self):
        return self.fullname +" "+self.eidikotita+" "+self.perioxi +" "+self.radevous

