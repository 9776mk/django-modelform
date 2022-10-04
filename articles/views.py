from django.shortcuts import render, redirect
from .models import Article

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

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # DB에 저장하는 로직
    title = request.GET.get('title')
    content = request.GET.get('content')
    # Models.py에서 생성한 DB(Article)에 저장하기
    # DB를 사용하기 위해 위쪽에 Article을 import 해오기
    Article.objects.create(title=title, content=content)
    
    return redirect('articles:index')