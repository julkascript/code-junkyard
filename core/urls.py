from django.urls import path

from core.views import index, post_create, post_details, post_edit

urlpatterns = [
    path('', index, name='home'),
    path('post-create/', post_create, name="post create"),
    path('post-details/<int:pk>', post_details, name="post details"),
    path('post-details/edit/<int:pk>', post_edit, name="post edit")
]
