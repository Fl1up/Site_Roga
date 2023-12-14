from django.contrib.auth.models import AnonymousUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.response import Response

from main.backend.models import Product, Cart, Order, Category
from main.backend.permissions import IsOwner
from main.backend.serializers import ProductSerializer, CartSerializer, OrderCreateSerializer, \
    CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    """Product List"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'price': ['gte', 'lte']
    }

    def get_queryset(self):
        category_id = self.request.query_params.get('category')
        return Product.objects.filter(category=category_id)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartListCreateAPIView(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):  # сохранения нового владельца
        new_foctors = serializer.save()
        print(self.request.headers)
        # new_foctors.owner = self.request.user  # owner - владелец  (нужно добавить в models)
        new_foctors.save()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'message': 'Регистрация пользователя успешна'}, status=status.HTTP_200_OK)


class CartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsOwner]

    def get_object(self):
        return Cart.objects.get(owner=self.request.user)


class OrderCreateAPIView(generics.CreateAPIView):
    """Order Create"""
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.get(owner=request.user)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            order = serializer.save(user=request.user)
            cart.products.clear()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryTreeView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AddProductToCartAPI(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]


class CategoryTreeView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
