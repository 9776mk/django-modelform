from django.urls import path
from . import views

app_name = 'articles'

# URL 설정을 app 단위로!
urlpatterns = [
    # http://127.0.0.1:8000/articles/
    path('', views.index, name='index'),
]