from rest_framework.routers import DefaultRouter
from django.urls import path
from main.backend.apps import BackendConfig
from main.backend.views import ProductListAPIView, ProductDetailAPIView, CartListCreateAPIView, \
    CartRetrieveUpdateDestroyAPIView, OrderCreateAPIView

# from main.backend.views import ProductListAPIView, ProductCreateAPIView

app_name = BackendConfig.name

router = DefaultRouter()

# все для Generic
urlpatterns = [
                  path("products/", ProductListAPIView.as_view(), name="product_category"),
                  path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
                  path('cart/', CartListCreateAPIView.as_view(), name='cart_list_create'),
                  path('cart/<int:pk>/', CartRetrieveUpdateDestroyAPIView.as_view(),
                       name='cart_retrieve_update_destroy'),
                  path('order/', OrderCreateAPIView.as_view(), name='order_create'),
              ] + router.urls
