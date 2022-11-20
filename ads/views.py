from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from ads.filters import AdsTitleFilter
from ads.models import Ad, Comment
from ads.permissions import OwnerOrAdminPermission
from ads.serializers import AdSerializer, AdDetailSerializer, CommentDetailSerializer, AdListSerializer, \
    CommentCreateSerializer, AdCreateSerializer, CommentUpdateSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    default_serializer = AdSerializer
    default_permission = [IsAuthenticated]
    pagination_class = AdPagination
    #подключение фильтрации
    filter_backends = [DjangoFilterBackend]
    filterset_class =AdsTitleFilter

    permission_classes_by_action = {"list": [AllowAny],
                                    "partial_update": [IsAuthenticated, OwnerOrAdminPermission],
                                    "destroy": [IsAuthenticated, OwnerOrAdminPermission],
                                    }

    serializer_classes = {"list": AdListSerializer,
                          "retrieve": AdDetailSerializer,
                          "create": AdCreateSerializer}

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self):
        return [perm() for perm in self.permission_classes_by_action.get(self.action, self.default_permission)]


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = AdPagination

    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(author=request.user.id)
        return super().get(request, *args, **kwargs)


class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    default_serializer = CommentDetailSerializer
    default_permission = [IsAuthenticated]

    serializer_classes = {"create": CommentCreateSerializer,
                          "partial_update": CommentUpdateSerializer
                          }

    permission_classes_by_action = {"partial_update": [IsAuthenticated, OwnerOrAdminPermission],
                                    "destroy": [IsAuthenticated, OwnerOrAdminPermission],
                                    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self):
        return [perm() for perm in self.permission_classes_by_action.get(self.action, self.default_permission)]

    def list(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        self.queryset = self.queryset.filter(ad=pk)
        return super(CommentsViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        pk_ad = kwargs.get('id')
        pk_comment = kwargs.get('pk')
        self.queryset = self.queryset.filter(ad=pk_ad, pk=pk_comment)
        return super(CommentsViewSet, self).retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        pk_ad = kwargs.get('id')
        pk_comment = kwargs.get('pk')
        self.queryset = self.queryset.filter(ad=pk_ad, pk=pk_comment)
        return super(CommentsViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        pk_ad = kwargs.get('id')
        pk_comment = kwargs.get('pk')
        self.queryset = self.queryset.filter(ad=pk_ad, pk=pk_comment)
        return super(CommentsViewSet, self).destroy(request, *args, **kwargs)
