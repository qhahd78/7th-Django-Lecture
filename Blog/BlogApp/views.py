from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
# Create your views here.


def portpolio(request):
    return render(request, 'portpolio.html')


def home(request):
    # 클래스 Blog 안에 있는 객체를 blogs 라는 변수에 저장.
    # 모델로부터 객체 목록을 전달 받을 수 있다.

    # 블로그의 모든 글이 대상
    blogs = Blog.objects  # 쿼리셋 #메소드
    # key 값 blogs 로 Blog의 객체를 받아 딕셔너리로 저장
    blog_list = Blog.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자른다.
    paginator = Paginator(blog_list, 3)
    # request 된 페이지가 뭔지 알아내고
    page = request.GET.get('page')
    # reqeust 된 페이지를 얻어온 뒤 return 한다. post에는 리퀘스트된 페이지에
    # 해당하는 번호가 들어간다.
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs, 'posts': posts})


def detail(request, blog_id):
    # 이용자가 원한 몇 번째 객체
    # 첫번째 인자 : 클래스 , 두번째 인지: pk 값
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html', {'blog': blog_detail})

    # 쿼리셋과 메소드(쿼리셋을 가공하는 역할) 형식
    # 모델.쿼리셋(objects).메소드

    # < 메소드 종류 >
    # .count: 객체 개수 반환
    # .first: 첫번째 객체 반환
    # .last: 마지막 객체 반환

# new.html 을 단순히 띄워주는 함수


def new(request):
    return render(request, 'new.html')

# 입력 받은 내용을 DB에 전달하는 함수


def create(request):
    # Blog 라는 클래스에 있는 객체를 받아 blog라는 변수에 저장.
    blog = Blog()
    # html 에서 입력 받은 title 값을 blog 라는 객체의 title 안에 담아줌.
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    # 쓴 시간을 blog 객체의 pub_date 변수에 저장.
    blog.pub_date = timezone.datetime.now()
    # blog(객체)에 여태 담은 내용들을 객체에 저장 객체.detete() 이런건 지워라.
    blog.save()
    # 데이터 처리 후에 redirect 에서 정한 경로로 곧장 이동한다.
    return redirect('/blog/'+str(blog.id))

    # redirect는 외부 링크도 가능. render 는 사이트 내의 링크로만 이동.
