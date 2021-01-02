from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    # create 함수를 실행시키기 위해 url 추가.
    path('create', views.create, name="create"),
]
