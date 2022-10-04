from django.urls import path
from . import views

app_name = 'articles'

# URL 설정을 app 단위로!
urlpatterns = [
    # http://127.0.0.1:8000/articles/
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/articles/new
    # ModelForm -> create와 new의 기능을 create에 합쳐서 더이상 필요없어졌음
    #path('new/', views.new, name='new'),
    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name='create'),

]