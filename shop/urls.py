from django.urls import path
from . import views
from rest_framework import renderers
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our OrderViewSet with it.
router = DefaultRouter()
router.register(r'orders', views.OrderViewSet, basename="orders")

urlpatterns = [
    path('stores/', views.getAllStores, name='stores'),
    path('stores/new/', views.newStore, name='new_store'),
    path('store/<str:pk>/', views.getStore, name='store'),
    path('store/<str:pk>/orders/', views.getStoreOrders, name='store_orders'),

    # The API URLs (Create,Read, Update, Delete) for orders
    # are now determined automatically by the router.
    path('', include(router.urls)),

]