from django.urls import path

from core.views import index, post_create, post_details

urlpatterns = [
    path('', index, name='home'),
    path('post-create/', post_create, name="post create"),
    path('post-details/<int:pk>', post_details, name="post details")
]
