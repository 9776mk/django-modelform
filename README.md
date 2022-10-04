# Django CRUD

## 1. 가상환경 및 Django 설치

### 1. 가상환경 생성 및 실행

- 가상환경 폴더를 `.gitignore`로 설정을 해둔다.

```bash
$ python -m venv venv
$ source venv/Scripts/activate
(venv) $
```

### 2. Django 설치 및 기록

```
$ pip install django==3.2.13
$ pip freeze > requirements.txt
```

### 3. Django 프로젝트 생성

```bash
$ django-admin startproject pjt .
```

#### 3.1 추가 설정
settings.py
```python
# django i18n 참고
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```


## 2. articles app

### 1. app 생성
```bash
$ django-admin startapp articles
```

### 2. app 등록
pjt/settings.py
```python
INSTALLED_APPS = [
    'articles',
]
```

### 3. urls.py 설정
#### 1. pjt/urls.py
```python
from django.urls import path, include #include 추가
# articles라는 주소로 들어오면 articles라는 앱에서 진행하고 싶어
# articles/urls.py에 있는 urlpatterns를 그대로 땡겨온다.
path('articles/', include('articles.urls'))
```

#### 2. articles/urls.py 생성

```python
# 추가적으로 활용하기 위해 name 설정
app_name = 'articles'

urlpatterns = [
  
]

```
## 3. Model 정의 (DB 설계)

### 1. 클래스 정의

### 2. 마이그레이션 파일 생성

### 3. DB 반영(`migrate`)

## 4. CRUD 기능 구현

### 1. 게시글 생성

> 사용자에게 HTML Form 제공, 입력받은 데이터를 처리 (ModelForm 로직으로 변경)

#### 1. HTML Form 제공

> http://127.0.0.1:8000/articles/new/

#### 2. 입력받은 데이터 처리

> http://127.0.0.1:8000/articles/create/

> 게시글 DB에 생성하고 index 페이지로 redirect

### 2. 게시글 목록

> DB에서 게시글을 가져와서, template에 전달

### 3. 상세보기

> 특정한 글을 본다.

> http://127.0.0.1:8000/articles/<int:pk>/

### 4. 삭제하기

> 특정한 글을 삭제한다.

> http://127.0.0.1:8000/articles/<int:pk>/delete/

### 5. 수정하기

> 특정한 글을 수정한다. => 사용자에게 수정할 수 양식을 제공하고(GET) 특정한 글을 수정한다.(POST)

> http://127.0.0.1:8000/articles/<int:pk>/update/