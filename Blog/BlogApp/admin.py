from django.contrib import admin
from .models import Blog
# Register your models here.

# models 에 만든 클래스를 어드민 사이트에 저장해준다
admin.site.register(Blog)