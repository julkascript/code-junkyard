from django.urls import path

from core.views import index, sign_in, sign_up

urlpatterns = [
    path('', index, name='home'),
    path('sign-in', sign_in, name="sign in"),
    path('sign-up', sign_up, name="sign up"),
]
