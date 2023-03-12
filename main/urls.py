from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_posts),
    path('/<int:pk>/', get_one_post),
    path('get-all-posts', get_all_posts),
    path('create-user/', create_person),
    path('create-comment/', create_comment),
    path('create-post/', create_post),
]
