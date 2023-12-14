from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from main.users.models import User
from main.users.permissions import IsOwner
from main.users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания пользователя"""

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(generics.ListAPIView):
    """Контроллер для списка пользователей"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]   # AllowAny # IsAuthenticated


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]   # AllowAny # IsAuthenticated


class UserUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для обновления пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwner, IsAdminUser]   # AllowAny # IsAuthenticated


class UserDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления пользователя"""

    queryset = User.objects.all()
    permission_classes = [IsOwner, IsAdminUser]   # AllowAny # IsAuthenticated
