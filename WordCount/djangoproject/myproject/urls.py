"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# views 파일 불러오기
import wordcount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # wordcount 안에, views 안에 있는 함수 실행. 
    path('', wordcount.views.home, name="home"),
    path('about/', wordcount.views.about, name="about"),
    path('result/', wordcount.views.result, name="result"),
]
