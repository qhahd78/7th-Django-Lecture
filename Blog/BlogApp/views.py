from django.shortcuts import render
from .models import Blog
# Create your views here.

def home(request):
    # 클래스 Blog 안에 있는 객체를 blogs 라는 변수에 저장.
    # 모델로부터 객체 목록을 전달 받을 수 있다. 
    blogs = Blog.objects #쿼리셋 #메소드
    # key 값 blogs 로 Blog의 객체를 받아 딕셔너리로 저장 
    return render(request, 'home.html', {'blogs': blogs})

    #쿼리셋과 메소드(쿼리셋을 가공하는 역할) 형식
    # 모델.쿼리셋(objects).메소드

    # < 메소드 종류 >
    #.count: 객체 개수 반환
    #.first: 첫번째 객체 반환
    #.last: 마지막 객체 반환