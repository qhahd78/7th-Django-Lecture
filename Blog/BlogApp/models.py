from django.db import models

# Create your models here.

class Blog(models.Model):
    # 변수 = 처리할 것들 (ex) title 이라는 변수는 텍스트 200자까지 들어가게 할거다
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    
    # object(1) 말고 타이틀이 뜨게 해주는 함수 
    def __str__(self):
        return self.title

# model. 웅앵Field(웅앵)