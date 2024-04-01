from django.urls import path
from .views import *
from .api import *
from Account import views

urlpatterns = [
    #path('signup/', UserSignupView.as_view(), name='signup'),
    #path('login/', UserLoginView.as_view(), name='login'),
    #path('logout/', UserLogoutView.as_view(), name='logout'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),


]
