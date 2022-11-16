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
    path('token/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('ads/', include("ads.urls")),
]

urlpatterns+=users_router.urls
urlpatterns+=router_ads.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)