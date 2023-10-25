from rest_framework.serializers import ModelSerializer
from models import CustomerModel, ProductModel, ItemsModel, CategoryModel, ShopCardModel
from rest_framework.exceptions import ValidationError


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class ItemsSerializer(ModelSerializer):
    class Meta:
        model = ItemsModel
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ShopCardSerializer(ModelSerializer):
    class Meta:
        model = ShopCardModel
        fields = '__all__'

    def to_representation(self, instance):
        if instance.total_price < 1_000_000:
            raise ValidationError('Total price must be more than one million')
        return super().to_representation(instance)

