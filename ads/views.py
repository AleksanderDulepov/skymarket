from rest_framework import pagination, viewsets
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    pass



class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    default_serializer = AdSerializer
    permission_classes = [IsAuthenticated]

    serializer_classes = {"retrieve":AdDetailSerializer,
                          "create":AdDetailSerializer}

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

