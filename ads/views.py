from rest_framework import pagination, viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentDetailSerializer, AdListSerializer, \
    CommentCreateSerializer


class AdViewSet(viewsets.ModelViewSet):
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









class ListCommentByAdvertView(ListAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentDetailSerializer

    def get(self, request, *args, **kwargs):
        pk=kwargs.get('pk')
        self.queryset=self.queryset.filter(ad=pk)
        return super().get(request, *args, **kwargs)


class DetailCommentByIdView(RetrieveAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentDetailSerializer

    def get(self, request, *args, **kwargs):
        # ad_pk=kwargs.get('pk')
        com_pk = kwargs.get('pk')
        self.queryset=self.queryset.filter(pk=com_pk)
        return super().get(request, *args, **kwargs)



class CreateCommentByUserView(CreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentCreateSerializer
    permission_classes = [IsAuthenticated]