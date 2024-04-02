from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='media/profile_pictures/', null=True, blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    notifications = models.ManyToManyField('Notification', related_name='user_notifications', blank=True)

    def get_notifications(self):
        return Notification.objects.filter(user=self)



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='media/post_images/', null=True, blank=True)
    video = models.FileField(upload_to='media/post_videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    comments = models.ManyToManyField(User, through='Comment', related_name='commented_posts')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)




class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)


class PrivacySettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post_privacy = models.CharField(max_length=20, choices=[('public', 'Public'), ('friends', 'Friends'), ('private', 'Private')], default='public')
    profile_privacy = models.CharField(max_length=20, choices=[('public', 'Public'), ('friends', 'Friends'), ('private', 'Private')], default='public')
    followers_privacy = models.CharField(max_length=20, choices=[('public', 'Public'), ('friends', 'Friends'), ('private', 'Private')], default='public')

    def __str__(self):
        return self.user.username + "'s Privacy Settings"
