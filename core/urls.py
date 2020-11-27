from django.urls import path

from core.views import index, post_create

urlpatterns = [
    path('', index, name='home'),
    # path('sign-in', sign_in, name="sign in"),
    # path('sign-up', sign_up, name="sign up"),
    path('post-create/', post_create, name="post create")
]
