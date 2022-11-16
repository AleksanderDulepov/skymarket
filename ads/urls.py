from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, AdListView, CreateCommentByUserView, ListCommentByAdvertView, DetailCommentByIdView

router_ads=SimpleRouter()
router_ads.register('ads', AdViewSet)

urlpatterns = [
    path('me/', AdListView.as_view()),
    path('<int:pk>/comments/<int:id>/', DetailCommentByIdView.as_view()),
    # path('<int:pk>/comments/', CreateCommentByUserView.as_view()),
    path('<int:pk>/comments/', ListCommentByAdvertView.as_view()),

]
