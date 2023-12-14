from django.contrib import admin

from main.backend.models import Product, Cart, Order


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
    )  # отображение на дисплее
    list_filter = ("name", "category", "price")  # фильтр
    search_fields = ("name", "category", "price")  # поля поиска

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "quantity",
        "products"
    )  # отображение на дисплее
    list_filter = ("owner", "quantity", "products")  # поля поиска


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "products",
        "amount",
    )  # отображение на дисплее
    list_filter = ("owner", "products", "amount")  # фильтр
    search_fields = ("owner", "products", "amount")  # поля поиска
