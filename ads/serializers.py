from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from ads.models import Ad, Comment
from users.models import User

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentDetailSerializer(serializers.ModelSerializer):
    author_first_name=serializers.CharField(max_length=150, required=False)
    author_last_name = serializers.CharField(max_length=150, required=False)
    author_image = serializers.CharField(max_length=150, required=False)

    class Meta:
        model = Comment
        fields = "__all__"


class CommentCreateSerializer(CommentDetailSerializer):
    author=serializers.SlugRelatedField(read_only=True, slug_field="id")
    ad=serializers.SlugRelatedField(read_only=True, slug_field="id")

    def create(self, validated_data):
        user_id=self.context['request'].user.id
        user_obj=get_object_or_404(User, pk=user_id)
        validated_data['author']=user_obj

        adv_id=self.context.get('view').kwargs.get('id')
        adv_obj=get_object_or_404(Ad, pk=adv_id)
        validated_data['ad']=adv_obj

        return super().create(validated_data)


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude=["created_at", "author"]


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name=serializers.CharField(max_length=150, required=False)
    author_last_name = serializers.CharField(max_length=150, required=False)

    class Meta:
        model = Ad
        fields = ["pk", "image","title","price","description","author_first_name","author_last_name","author"]



class AdCreateSerializer(AdDetailSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="id")

    def create(self, validated_data):
        user_id = self.context['request'].user.id  # так достаем инфу о request.user
        user_obj = get_object_or_404(User, pk=user_id)
        validated_data['author'] = user_obj  # добавляем в словарь перед сохранением
        return super().create(validated_data)


class CommentUpdateSerializer(CommentDetailSerializer):

    created_at=serializers.DateTimeField(read_only=True)
    id=serializers.IntegerField(read_only=True)

    author=serializers.SlugRelatedField(read_only=True, slug_field="id")
    ad=serializers.SlugRelatedField(read_only=True, slug_field="id")