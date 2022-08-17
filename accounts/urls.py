from django.urls import path,include
from .views import *
from .models import *

urlpatterns = [
    path("register", registration, name="account_registration"),
    path('login', LoginAuthToken.as_view(), name='account_login'),

]