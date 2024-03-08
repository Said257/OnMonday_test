from django.urls import path
from .views import UserListAPI


urlpatterns = [
    path('list/', UserListAPI.as_view()),
]
