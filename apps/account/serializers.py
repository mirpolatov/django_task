from rest_framework.serializers import ModelSerializer

from account.models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id',)
