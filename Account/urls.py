from django.urls import path
from .views import *
from .api import *
from Account import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('signup/', UserSignupView.as_view(), name='signup'),
    #path('login/', UserLoginView.as_view(), name='login'),
    #path('logout/', UserLogoutView.as_view(), name='logout'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
    
    path('accounts/login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('update_profile/', views.update_profile_view, name='update_profile'),
    path('user_search/', views.user_search_view, name='user_search'),
    

    path('create_post/', views.create_post_view, name='create_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('comment_post/<int:post_id>/', views.comment_post, name='comment_post'),

    path('follow_user/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow_user/<int:user_id>/', views.unfollow_user, name='unfollow_user'),

    path('notifications/', views.notifications_view, name='notifications'),
    path('mark_notification_as_read/<int:notification_id>/', views.mark_notification_as_read, name='mark_notification_as_read'),

    path('send_message/<int:receiver_id>/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('conversation/<int:receiver_id>/', views.conversation, name='conversation'),
    path('mark_as_read/<int:message_id>/', views.mark_as_read, name='mark_as_read'),


]

