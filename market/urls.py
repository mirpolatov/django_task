from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CustomerAPIView, CategoryAPIView, ProductAPIView, ShopCardAPIView, ItemsAPIVIew
from .views import PriceSum

router = DefaultRouter()
router.register('customer', CustomerAPIView, 'customer')
router.register('category', CategoryAPIView, 'category')
router.register('product', ProductAPIView, 'product')
router.register('shop-card', ShopCardAPIView, 'shop-card')
router.register('items', ItemsAPIVIew, 'items')

urlpatterns = [*router.urls,
               path('price-sum', PriceSum.as_view()), ]
# path('product_count', Prodcut_count.as_view()), ]
