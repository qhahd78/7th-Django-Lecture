from django.db import models

# Create your models here.


class Portpolio(models.Model):
    title = models.CharField(max_length=255)
    # 이미지를 받아주는 필드
    # 이미지 필드 넣을거면 pip install pillow 해야함.
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
