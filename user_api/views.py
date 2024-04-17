from django.http import JsonResponse 
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
 
@api_view(['GET','POST'])
def user(request, user_id=None):

    if request.method == 'GET':
        if user_id is not None:
            '''
            Returns only a user specified by a requested user_id
            '''
            user = get_object_or_404(User, pk=user_id)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
