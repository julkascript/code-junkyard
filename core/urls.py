from django.urls import path

from core.views import index, post_create, post_details, post_edit, post_list, post_delete

urlpatterns = [
    path('', index, name='home'),

    # post logic
    path('post-create/', post_create, name="post create"),
    path('post-list/', post_list, name="post list"),
    path('post-details/<int:pk>', post_details, name="post details"),
    path('post-details/edit/<int:pk>', post_edit, name="post edit"),
    path('post-delete/<int:pk>', post_delete, name="post delete"),
]
