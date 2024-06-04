from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from .serializers import UserSerializer
from .models import User
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if email is None or password is None:
        return Response({'message': 'Please provide both email and password',
                         'success': False},
                        status=400)
    user = User.objects.filter(email=email).first()
    if not user:
        return Response({'message': 'Invalid Credentials',
                         'success': False},
                        status=404)
    if not user.check_password(password):
        return Response({'message': 'Invalid Credentials',
                         'success': False},
                        status=404)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'message': 'Login successful',
                        'success': True,
                        'token': token.key})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def get_user(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response({"user": serializer.data})

@api_view(['GET'])
def get_user_by_id(request, id):
    user = get_object_or_404(User, pk=id)
    serializer = UserSerializer(user)
    return Response({"user": serializer.data})



@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def testtoken(request):
    return Response("passed for {}".format(request.user.username))