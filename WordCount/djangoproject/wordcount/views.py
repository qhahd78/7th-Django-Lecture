from django.shortcuts import render

# Create your views here.
# render: 3개의 인자. 1. request 고정 2. 템플릿 위치
# 3. 딕셔너리 형도 가능 

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    # get 으로 받음
    # fulltext 로 입력한 전체 문장 받아서 text에 저장.
    text = request.GET['fulltext']
     # 공백 기준으로 쪼개서 리스트에 넣어주는 함수 .split()
    words = text.split()
    word_dictionary = {}

    #word 는 새 변수고, words 리스트 안에 요소만큼 반복문. 
    for word in words:
        #만약에 word_dictionary에 해당 word 가 있으면 value값 +1 
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        # 해당 word 없으면 id는 word 자체로, value 값 1로 추가 해주기 
        else: 
            #add to dictionary
            word_dictionary[word]=1 

    # 총 단어수 = len(words) words에 저장된 리스트의 길이. 
     # key 값은 full, value 값은 받은 text로 result 로 보낸다.
    return render (request, 'result.html' , {'full':text, 'total': len(words), 'dictionary': word_dictionary})





# 리스트를 쭉 돌면서 각 단어당 키 값을 '단어' 로, 키 값을 1로 준다. 
# 만약 똑같은 단어가 나오면 value 값을 1씩 높여 가는 방식으로 동일 단어 수를 카운트 한다. 