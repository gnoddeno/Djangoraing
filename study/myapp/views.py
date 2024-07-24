from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer
from .models import User

@api_view(['GET'])
def getUser(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request, name):
    try:
        user = User.objects.get(name=name)
    except User.DoesNotExist:
        return Response({'error' : {
            'code' : 404,
            'message' : 'User not found'
        }}, status=status.HTTP_404_NOT_FOUND)
    user = UserSerializer(user, data=request.data)
    if user.is_valid():
        user.save()
        return Response(user.data)
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request, name):
    try:
        user = User.objects.get(name=name)
    except User.DoesNotExist:
        return Response({'error' : {
            'code' : 404,
            'message' : 'User not found'
        }}, status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, name):
        try:
            user = User.objects.get(name=name)
        except User.DoesNotExist:
            return Response({'error' : {
                'code' : 404,
                'message' : 'User not found'
            }}, status=status.HTTP_404_NOT_FOUND)
        user = UserSerializer(user, data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        try:
            user = User.objects.get(name=name)
        except User.DoesNotExist:
            return Response({'error' : {
                'code' : 404,
                'message' : 'User not found'
            }}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)