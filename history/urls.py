from django.urls import path
from .views import *

urlpatterns = [
    path('account/', current_account),
]