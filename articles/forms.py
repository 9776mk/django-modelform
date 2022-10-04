from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        # Aricle에 있는 것을 모델로 해서
        model = Article
        # 모든 것들을 필드로 불러온다.
        fields = '__all__'
        # 만약 타이들만 하고 싶다면 fields = ['title']
        # 만약 타이들과 컨텐츠를 하고 싶다면 fields = ['title', 'content']