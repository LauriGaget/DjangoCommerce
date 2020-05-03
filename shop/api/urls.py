from django.urls import path
from shop.api.view import ProductListCreateAPIView, ProductDetailAPIView


urlpatterns = [
    path("product/", ProductListCreateAPIView.as_view(), name="product-list"),
    path("product/<int:pk>", ProductDetailAPIView.as_view(), name="product-detail")

]
