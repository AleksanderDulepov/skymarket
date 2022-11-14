from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name="Автор обьявления",
                               related_name="ad_author")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"


class Comment(models.Model):
    text = models.CharField(max_length=150)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name="Автор комментария",
                               related_name="com_author")
    ad = models.ForeignKey(Ad,
                           on_delete=models.CASCADE,
                           verbose_name="Обьявление с комментарием",
                           related_name="com_advert")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"