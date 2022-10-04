from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm # ModelForm을 사용하기 위한 코드 추가

# Create your views here.

# 요청 정보를 받아서
def index(request):
    # 게시글을 가져와서
    # articles = Article.objects.all()
    articles = Article.objects.order_by('-pk')
    
    # Template에 전달한다.
    context = {
        'articles': articles
    }

    # 페이지를 render
    return render(request,'articles/index.html', context)

# 63번째 # !def new 함수 주석 처리! 
# index.html, urls에서 new 없애기!
# def new(request):
#      # ModelForm용 추가 코드
#     article_form = ArticleForm()
#     context = {
#         'article_form': article_form
#     }
#     #return render(request, 'articles/new.html')
#     return render(request, 'articles/new.html', context=context)


''' New + Create 합치기 전 코드
def create(request):
    # DB에 저장하는 로직
    # GET을 사용할 때 받는 방법
    ### ModelForm 사용 전
    # title = request.GET.get('title')
    # content = request.GET.get('content')

    # POST를 사용할 때는 POST.get으로 바꿔줘야 함!
    title = request.POST.get('title')
    content = request.POST.get('content')

    # Models.py에서 생성한 DB(Article)에 저장하기
    # DB를 사용하기 위해 위쪽에 Article을 import 해오기
    Article.objects.create(title=title, content=content)
    ### ModelFrom 사용전 끝
    article_form = ArticleForm(request.POST)

    # 유효성 검사
    if article_form.is_valid():
        article_form.save()
        return redirect('articles:index')
    else:
        #print('유효하지 않습니다.')
        # 유효하지 않을 때 무엇을 하면 좋을까?
        # form 페이지에 메시지를 띄워서 사용자에게 보여주기!
        # new 함수에 있는 내용을 붙여넣기
        context = {
            'article_form': article_form
        }
        #return render(request, 'articles/new.html')
        return render(request, 'articles/new.html', context=context)
'''

# new 함수와 create 함수가 같아보이기 때문에 합친다!
# !def new 함수 주석 처리!

def create(request):
    # method가 POST인 경우
    if request.method == 'POST':
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    # method가 GET인 경우
    else:
        article_form = ArticleForm()
    # invalid일 경우 74번째에서 아랫줄로 바로 내려감. 들여쓰기 주의!    
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)