from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class LoginAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


@api_view(['POST'])
def registration(request):
    data = request.data
    user = RegistrationSerializer(data=data)
    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
           user = User.objects.create(
               username = data['username'],
               email = data['email'],
               password = make_password(data['password'])
           ) 
           return Response({
                'message': 'User registered.'},
                status=status.HTTP_200_OK
            )
        else:
            return Response({
                'error': 'User already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(user.errors)
