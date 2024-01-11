from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer
from .functions import (
    get_user_response,
    create_user_response,
    update_user_response,
    update_user_response_by_nickname,
    delete_user_response
)

import json

@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':

        users = User.objects.all()                          #NOTE - get all objects in User's DB 

        serializer = UserSerializer(users, many=True)       #NOTE - serialize the object data into json 

        return Response(serializer.data)                    #NOTE - return the serialized data
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def get_by_nick(request, nick):

    try:
        user = User.objects.get(pk=nick)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return get_user_response(user)

    elif request.method == 'PUT':
        return update_user_response(user, request.data)


#SECTION CRUD 
    
@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request):

    if request.method == 'GET':
        try:
            UserNickname = request.GET['user']         #NOTE - find the parameter
            user = User.objects.get(pk=UserNickname)   #NOTE - get the object data in DB
            return get_user_response(user)
        except (KeyError, User.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            

#NOTE - POST, creating data by the function in functions.py

    if request.method == 'POST':
        return create_user_response(request.data)

#NOTE - PUT, edit data by the function in functions.py

    if request.method == 'PUT':
        return update_user_response_by_nickname(request.data)

#NOTE - DELETE, delete data by the function in functions.py

    if request.method == 'DELETE':
        return delete_user_response(request.query_params.get('user'))





#NOTE - Django's functions to use with data
        
# def DjangoDB():

#     data = User.objects.get(pk='oliver123')          #NOTE - object

#     data = User.objects.filter(user_age='35')           #NOTE - queryset

#     data = User.objects.exclude(user_age='35')          #NOTE - queryset

#     data.save()

#     data.delete()