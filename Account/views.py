

from Account.models import Post, User


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse





def home_view(request):
    # Assuming you have a Post model to fetch recent posts
    posts = Post.objects.all().order_by('-created_at')[:10]
    return render(request, 'Account/Home.html', {'posts': posts})

@login_required
def profile_view(request):
    return render(request, 'Account/Profile.html', {'user': request.user})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'Account/Login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect(reverse('home'))
    return render(request, 'Account/Signup.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))
