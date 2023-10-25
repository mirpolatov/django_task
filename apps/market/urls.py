from django.urls import path, include
from market import views
from rest_framework.routers import DefaultRouter

from market.views import PriceSum, Prodcut_count

router = DefaultRouter()
router.register('customer', views.CustomerAPIView, 'customer')
router.register('category', views.CategoryAPIView, 'category')
router.register('product', views.ProductAPIView, 'product')
router.register('shop-card', views.ShopCardAPIView, 'shop-card')
router.register('items', views.ItemsAPIVIew, 'items')

urlpatterns = [*router.urls,
               path('price-sum', PriceSum.as_view()),
               path('product_count', Prodcut_count.as_view()), ]
