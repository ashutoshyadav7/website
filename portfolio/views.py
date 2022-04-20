from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    if request.user.is_authenticated:
    # Do something for authenticated users.
    
     return render(request, 'profile.html')
    else:
    # Do something for anonymous users.
     return redirect('/auth')

def userAuth(request):

    if request.user.is_authenticated:
    # Do something for authenticated users.
    
     return redirect('/profile')
    else:    
     return render(request, 'authenticate.html')

def userRegi(request):

    if request.user.is_authenticated:
    
     return redirect('/profile')
    else:

     if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password)
        user.username = username
        user.password = password

        user.save()
  
    
     return redirect('/login')

def loginUser(request):

    if request.user.is_authenticated:
    # Do something for authenticated users.
    
     return redirect('/profile')
    else:

     if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            name=user.username
            return redirect('/profile', {'name': name})
        else:
            messages.error(request, "Wrong Credentials")
    
    return redirect('/auth')

def logOut(request):

    if request.user.is_authenticated:
    # Do something for authenticated users.
        logout(request)
    
        return redirect('/')
    else:

        return render(request, 'authenticate.html')

    