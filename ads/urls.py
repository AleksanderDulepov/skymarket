from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, CommentViewSet

router_ads=SimpleRouter()
router_ads.register('ads', AdViewSet)
router_ads.register('comments', CommentViewSet)
