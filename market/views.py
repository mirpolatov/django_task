from tkinter.messagebox import RETRY

from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import CategoryModel, CustomerModel, ProductModel, ShopCardModel, ItemsModel
from .permission import AdminOrOwnerPermissionClass, UserPermissionClass, AdminPermissionClass
from .serializers import CategorySerializer, CustomerSerializer, ProductSerializer, ShopCardSerializer, \
    ItemsSerializer


class CategoryAPIView(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (AdminOrOwnerPermissionClass, )


class CustomerAPIView(ModelViewSet):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [UserPermissionClass | AdminPermissionClass]


class ProductAPIView(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AdminOrOwnerPermissionClass | UserPermissionClass]


class ShopCardAPIView(ModelViewSet):
    queryset = ShopCardModel.objects.all()
    serializer_class = ShopCardSerializer
    permission_classes = [AdminOrOwnerPermissionClass | UserPermissionClass]


class PriceSum(RetrieveAPIView):
    serializer_class = ProductSerializer
    http_method_name = 'get'

    def retrieve(self, *args, **kwargs):
        return Response(ProductModel.get_all_price())


# class Prodcut_count(RetrieveAPIView):
#     serializer_class = ProductSerializer
#     http_method_name = 'get'
#
#     def retrieve(self, *args, **kwargs):
#         return Response(ProductModel.prduct_count)


class ItemsAPIVIew(ModelViewSet):
    queryset = ItemsModel.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = (AdminOrOwnerPermissionClass,)
