from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def signup(request):
    if request.method == 'POST':
        # POST 방식으로 변수 가져올 때 request.POST,
        # GET 방식으로 변수 가져올 때 request.GET
        if request.POST['password'] == request.POST['password2']:
            # create_user 함수 불러와서 user 생성해줌
            user = User.objects.create_user(
                # username, userpassword 모두 POST 방식의 변수를 가져와서 유저를 생성해줌
                username=request.POST['username'], password=request.POST['password'])
            # 로그인을 하기 위해 불러오는 함수.
            auth.login(request, user)
            # 다 되면 home으로 이동
            return redirect('home')
    # if 에 맞지 않는 조건이면 signup 에 머무른다.
    return render(request, 'signup.html')


def login(request):
    # POST 방식으로 리퀘스트가 왔다면,
    # username 이라는 변수에 username 을 받아 저장.
    # password 라는 변수에 password 을 받아 저장.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 입력한 username과 password 가 서버에 있는 회원인지 확인하는 함수.
        # 이 결과 (회원이다. 아니다.) 를 user 에 넣어준다.
        user = auth.authenticate(request, username=username, password=password)
        # 만약 유저가 없는 유저가 아니라면. (DB에 있는 유저라면. 로그인이 된다. )
        if user is not None:
            # 로그인이 된다.
            auth.login(request, user)
            # home으로 바로 redirect
            return redirect('home')
        else:
            # 없는 유저라면, error 출력.
            return render(request, 'login.html', {'error': 'username or passwords incorrect.'})
    # 포스트 방식도 아니고,, 뭔가 오류 나면. login 페이지로.
    else:
        return render(request, 'login.html')


def logout(request):
    if request.mothod == "POST":
        auth.logout(reqeust)
        return redirect('home')
    return render(request, 'login.html')
