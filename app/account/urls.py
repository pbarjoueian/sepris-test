
from django.urls import include, path

from .api import RegisterApi

urlpatterns = [
    path('account/register', RegisterApi.as_view()),
]
