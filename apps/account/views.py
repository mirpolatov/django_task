from rest_framework.viewsets import ModelViewSet

from models import CustomUser
from serializers import UserSerializer


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    http_method_names = 'GET'

    def get(self, pk):
        queryset = CustomUser.objects.filter(pk=pk)
