from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account import views

router = DefaultRouter()
router.register('user', views.UserView, 'user')

urlpatterns = [
    path('user/', include(router.urls)),

]
