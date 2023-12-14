from rest_framework import serializers
from rest_framework import generics
from .models import Category
from main.backend.models import Product, Cart, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

        def get_queryset(self):
            queryset = Product.objects.all()
            category = self.request.query_params.get('category', None)
            if category is not None:
                queryset = queryset.filter(category=category)
            return queryset


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        factors_item = Product.objects.create(**validated_data)
        return factors_item


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data):
        factors_item = Cart.objects.create(**validated_data)
        return factors_item




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def perform_create(self, serializer):
        cart = Cart.objects.get(owner=self.request.user)
        order = serializer.save(owner=self.request.user)
        order.products.set(cart.products.all())
        cart.products.clear()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"