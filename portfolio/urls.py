from django.urls import path
from . import views 

urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('auth/', views.userAuth, name='loginRegPage'),
    path('register', views.userRegi, name='registerUser'),
    path('login', views.loginUser, name='loginUser'),
    path('logout/', views.logOut, name='logoutUser'),

]
