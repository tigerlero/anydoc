from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('signin/', views.signin, name = 'signin'),
    path('contact/', views.contact, name = 'contact'),
    path('radevus/', views.radevus, name = 'radevus'),
    path('radevou/', views.radevou, name = 'radevou'),
    path('radevou2/', views.radevou2, name='radevou2'),
    path('radevou3/', views.radevou3, name = 'radevou3'),
    path('radevou4/', views.radevou4, name = 'radevou4'),
    path('resetpass/', views.resetpass, name = 'resetpass'),
    path('400/', views.handler400, name = '400'),
    path('403/', views.handler403, name = '403'),
    path('404/', views.handler404, name = '404'),
    path('500/', views.handler500, name = '500'),
    path('signup/', views.signup, name = 'signup'),
    path('signout/', views.signout, name = 'signout'),
    #path('singout/', 'django.contrib.auth.views.logout', {'next_page': '/signin'}),

]
#    path('radevou/<str:eidikotita>/<str:perixoi>', views.radevou2, name = 'radevou2'),
#    path('radevou/<str:fullname>/<str:eidikotita>/<str:perixoi>', views.radevou3, name = 'radevou3'),
#    path('radevou/<str:fullname>/<str:eidikotita>/<str:perixoi>/<str:radevou>', views.fradevou, name = 'fradevou'),