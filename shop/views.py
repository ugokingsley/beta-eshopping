from rest_framework import viewsets, permissions
from django.shortcuts import render
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg, Min, Max, Count
from .serializers import *
from .models import *
from accounts.models import *
from django.shortcuts import get_object_or_404
from django.db.models import Count, Exists, OuterRef



# get all stores
@api_view(['GET'])
def getAllStores(request):
	queryset = Store.objects.all().order_by('-id')
	serializer = StoreSerializer(queryset, many=True)
	return Response({
        'stores': serializer.data,
     })

# create a store
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newStore(request):
	request.data['store_admin'] = request.user
	data = request.data
	store = Store.objects.create(**data)
	serializer = StoreSerializer(store, many=False)
	return Response(serializer.data)

# get individual store
@api_view(['GET'])
def getStore(request, pk):
    store = get_object_or_404(Store, id=pk)
    serializer = StoreSerializer(store, many=False)
    return Response({
    	'store': serializer.data
    })

# get individual store orders
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getStoreOrders(request, pk):
    user = request.user
    store = get_object_or_404(Store, id=pk)
    orders = store.order_set.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)



class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for orders.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['store','user','order_state']
    
    def create(self, request):
        serializer = OrderSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True) 
        serializer.save(user=request.user)
        return Response(serializer.data)
        