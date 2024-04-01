

from django.forms import ValidationError
from Account.models import Post, User


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .models import Notification, Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

from .models import Post, Comment,Message
from .forms import CommentForm, LikeForm








@login_required
def home_view(request):
    posts = Post.objects.all().order_by('-created_at')[:10]
    comment_form = CommentForm() 
    return render(request, 'Account/Home.html', {'posts': posts, 'comment_form': comment_form})

@login_required
def profile_view(request):
    return render(request, 'Account/Profile.html', {'user': request.user})

@login_required
def update_profile_view(request):
    if request.method == 'POST':
        request.user.name = request.POST.get('name', '')
        request.user.email = request.POST.get('email', '')
        request.user.profile_picture = request.FILES.get('profile_picture')
        request.user.save()
        return redirect(reverse('profile'))
    return render(request, 'Account/update_profile.html', {'user': request.user})

@login_required
def user_search_view(request):
    query = request.GET.get('q', '')
    if query:
        users = User.objects.filter(username__icontains=query)
    else:
        users = User.objects.all()
    return render(request, 'Account/user_search.html', {'users': users, 'query': query})



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

@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            video = form.cleaned_data.get('video')
            if image and video:
                raise ValidationError("You can only upload either an image or a video, not both.")
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'Account/create_post.html', {'form': form})


@login_required
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = LikeForm(request.POST)
        if form.is_valid():
            if request.user in post.likes.all():
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
            return redirect('home')
    return redirect('home')

@login_required
def comment_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(user=request.user, post=post, text=form.cleaned_data['text'])
            comment.save()
            return redirect('home')
    return redirect('home')


@login_required
def follow_user(request, user_id):
    user_to_follow = User.objects.get(id=user_id)
    request.user.following.add(user_to_follow)
    return redirect('profile', user_id=user_id)

@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = User.objects.get(id=user_id)
    request.user.following.remove(user_to_unfollow)
    return redirect('profile', user_id=user_id)


@login_required
def notifications_view(request):
    notifications = request.user.notifications.all()
    return render(request, 'Account/notifications.html', {'notifications': notifications})

@login_required
def mark_notification_as_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.read = True
    notification.save()
    return redirect('notifications')


@login_required
def send_message(request, receiver_id):
    if request.method == 'POST':
        receiver = User.objects.get(id=receiver_id)
        message_text = request.POST.get('message')
        Message.objects.create(sender=request.user, receiver=receiver, message=message_text)
        return redirect('inbox')
    return redirect('inbox')

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'Account/inbox.html', {'messages': messages})

@login_required
def conversation(request, receiver_id):
    receiver = User.objects.get(id=receiver_id)
    messages = Message.objects.filter(sender=request.user, receiver=receiver).order_by('timestamp')
    return render(request, 'Account/conversation.html', {'receiver': receiver, 'messages': messages})

@login_required
def mark_as_read(request, message_id):
    message = Message.objects.get(id=message_id)
    message.read = True
    message.save()
    return redirect('inbox')