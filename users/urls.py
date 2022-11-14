from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView


users_router=SimpleRouter()
users_router.register('users', UserViewSet, basename='users')


