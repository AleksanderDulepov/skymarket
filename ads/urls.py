from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, AdListView,CommentsViewSet

router_ads=SimpleRouter()
router_ads.register('api/ads', AdViewSet)
router_comments_set=SimpleRouter()
router_comments_set.register('comments', CommentsViewSet)


urlpatterns = [
    path('me/', AdListView.as_view()),
    path('<int:id>/', include(router_comments_set.urls)),
]
