from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from main.users.models import User

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    category = models.CharField(max_length=100, verbose_name="Категория")
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return f"{self.name} {self.category}"

    class Meta:
        verbose_name = "Продукт "
        verbose_name_plural = "Продукты"


class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    quantity = models.IntegerField(verbose_name="Количество")
    products = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")

    def __str__(self):
        return f"{self.owner} {self.quantity} {self.products}"

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    products = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт", **NULLABLE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Количество ")

    def __str__(self):
        return f"{self.owner} {self.products}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='Патерн')

    class MPTTMeta:
        order_insertion_by = ['name']
