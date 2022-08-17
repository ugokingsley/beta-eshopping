from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.conf.urls.static import static
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import *
from shop.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('shop/', include('shop.urls')),
]
