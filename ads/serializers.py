from rest_framework import serializers

from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name=serializers.CharField(max_length=150, required=False)
    author_last_name = serializers.CharField(max_length=150, required=False)

    class Meta:
        model = Ad
        fields = ["pk", "image","title","price","description","author_first_name","author_last_name","author"]

