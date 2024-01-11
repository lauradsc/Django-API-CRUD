from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

def get_user_response(user):
    serializer = UserSerializer(user)
    return Response(serializer.data)


def create_user_response(user_data):
    serializer = UserSerializer(data=user_data)
    if serializer.is_valid(): #NOTE - serializer's function to validate data
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


def update_user_response(user, data):
    serializer = UserSerializer(user, data=data) #NOTE - serialize object data into json
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)  #NOTE - return the serialized data
    return Response(status=status.HTTP_400_BAD_REQUEST)


def update_user_response_by_nickname(data):
    nickname = data.get('user_nickname')
    try:
        user = User.objects.get(pk=nickname)
        return update_user_response(user, data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def delete_user_response(nickname):
    try:
        user = User.objects.get(pk=nickname)
        user.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  
      


