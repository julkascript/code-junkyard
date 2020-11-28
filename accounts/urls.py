from django.urls import path
from accounts.views import signup_user, signout_user, signin_user, user_profile

urlpatterns = [
    path('signin/', signin_user, name='user signin'),
    path('signup/', signup_user, name='user signup'),
    path('signout/', signout_user, name='user signout'),
    path('profile/<int:pk>', user_profile, name='user profile')
]
