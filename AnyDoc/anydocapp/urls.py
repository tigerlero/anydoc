from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('signin/', views.signin, name = 'signin'),
    path('contact/', views.contact, name = 'contact'),
    path('radevou/', views.radevou, name = 'radevou'),
    path('radevou/<str:eidikotita>/<str:perixoi>', views.radevou, name = 'radevou'),
    path('radevou/<str:fullname>/', views.radevou, name = 'radevou'),
    path('radevou/<str:description>', views.radevou, name = 'radevou'),
    path('resetpass/', views.resetpass, name = 'resetpass'),
    path('400/', views.handler400, name = '400'),
    path('403/', views.handler403, name = '403'),
    path('404/', views.handler404, name = '404'),
    path('500/', views.handler500, name = '500'),
    path('signup/', views.signup, name = 'signup'),
    path('signin/', views.signout, name = 'signout'),

]