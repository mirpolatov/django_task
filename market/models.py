from django.db import models


class CustomerModel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150, default='Tashkent')
    email = models.CharField(max_length=200, default=' ')
    number = models.BigIntegerField(default=10)
    date = models.DateField(default='24-10-2023')

    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')

    def __str__(self) -> str:
        return self.name


class ShopCardModel(models.Model):
    date = models.DateField(default='24-10-2023')
    owner = models.CharField(max_length=100)
    total_price = models.BigIntegerField(default=1000)
    payment = models.CharField(max_length=100, default='payment')
    customer = models.ForeignKey('CustomerModel', on_delete=models.CASCADE, related_name='customer')


class ProductModel(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey('CategoryModel', on_delete=models.CASCADE, related_name='category')
    price = models.BigIntegerField(default=1000)
    start_date = models.DateField(default='24-10-2023')
    end_date = models.DateField(default='24-10-2023')

    @staticmethod
    def get_all_price():
        return ProductModel.objects.aggregate(models.Sum('price'))

    def __str__(self) -> str:
        return self.name


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    total = models.BigIntegerField(default=1000)

    def __str__(self) -> str:
        return self.name


class ItemsModel(models.Model):
    product = models.ForeignKey('ProductModel', on_delete=models.CASCADE, related_name='items')
    shop_card = models.ForeignKey('ShopCardModel', on_delete=models.CASCADE, related_name='shop_card')
    sell_date = models.DateField(default='24-10-2023')
