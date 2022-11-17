from rest_framework import pagination, viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentDetailSerializer, AdListSerializer, \
    CommentCreateSerializer


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    default_serializer = AdSerializer
    permission_classes = [IsAuthenticated]

    serializer_classes = {"list":AdListSerializer,
                          "retrieve":AdDetailSerializer,
                          "create":AdDetailSerializer}

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)


class AdListView(ListAPIView):
    queryset=Ad.objects.all()
    serializer_class=AdListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(author=request.user.id)
        return super().get(request, *args, **kwargs)



class CommentsViewSet(ModelViewSet):
    queryset=Comment.objects.all()
    default_serializer=CommentDetailSerializer
    permission_classes = [IsAuthenticated]

    serializer_classes = {"create": CommentCreateSerializer}

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)


    def list(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        self.queryset = self.queryset.filter(ad=pk)
        return super(CommentsViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        pk_ad = kwargs.get('id')
        pk_comment = kwargs.get('pk')
        self.queryset = self.queryset.filter(ad=pk_ad, pk=pk_comment)
        return super(CommentsViewSet, self).retrieve(request, *args, **kwargs)



#обьявления http://localhost:8000/api/ads/
# http://localhost:8000/api/{id}
# http://localhost:8000/api/me/

#комменты http://localhost:8000/api/api/{ad_pk}/comments/
#http://localhost:8000/api/ads/{ad_pk}/comments/{id}/