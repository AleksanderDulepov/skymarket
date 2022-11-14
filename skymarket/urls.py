from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ads.urls import router_ads
from users.urls import users_router

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path('users/login/', TokenObtainPairView.as_view()), #тут можно поизящнее
    path('users/login/refresh/', TokenRefreshView.as_view()),    #тут можно поизящнее
]

urlpatterns+=users_router.urls
urlpatterns+=router_ads.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)