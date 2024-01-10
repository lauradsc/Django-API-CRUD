from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

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
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == 'PUT':

        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)




#SECTION CRUD 
    
@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request):

    if request.method == 'GET':

        try:
            if request.GET['user']:                         #NOTE - check if there's a parameter called user (/?user=xxxx&...)

                UserNickname = request.GET['user']         #NOTE - find the parameter

                try:
                    User = User.objects.get(pk=UserNickname)   #NOTE - get the object data in DB
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = UserSerializer(User)           #NOTE - serialize object data into json
                return Response(serializer.data)            #NOTE - return the serialized data

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

#NOTE - POST, creating data

    if request.method == 'POST':

        NewUser = request.data
        
        serializer = UserSerializer(data=NewUser)

        if serializer.is_valid(): #NOTE - serializer's function to validate data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)




#NOTE - PUT, edit data

    if request.method == 'PUT':

        Nickname = request.data['user_nickname']

        try:
            UpdateUser = User.objects.get(pk=Nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        print(request.data)

        serializer = UserSerializer(UpdateUser, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)




#NOTE - DELETE, delete data

    if request.method == 'DELETE':

        Nickname = request.query_params.get('user')

        try:
            UserToDelete = User.objects.get(pk=Nickname)
            UserToDelete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)









#NOTE - Django's functions to use with data
        
# def DjangoDB():

#     data = User.objects.get(pk='oliver123')          #NOTE - object

#     data = User.objects.filter(user_age='35')           #NOTE - queryset

#     data = User.objects.exclude(user_age='35')          #NOTE - queryset

#     data.save()

#     data.delete()