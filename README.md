[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![](https://img.shields.io/badge/django-3.2.2-green)
![](https://img.shields.io/badge/HTML-pink)
![](https://img.shields.io/badge/CSS-blue)
![](https://img.shields.io/badge/JS-yellow)
![](https://img.shields.io/badge/Pillow-8.2.0-red)

# Fancy coder
**Fancy coder**`s cool Project

## Contributor
- Likelion in Chungang University
 
|    Name    | Email                                        |
| :-----------: | :------------------------------------------------- |
|    최윤한(Leader)     |unusualc@likelion.org | 
|    인세훈     | dlstpgns0406@gmail.com |
|    민정호     |alswjdgh5095@gmail.com |
|    박채연     | 
|    이성민     | 
 
## Service
### How to
```console
$ git clone https://github.com/LikeLion-CAU-9th/Django-project-Daman.git
$ git pull origin develop
$ python -m venv myvenv
$ source myvenv/scripts/activate  mac) source myvenv/bin/activate
$ cd Webeing
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver
```
#### Module installation
```console
$ pip install -r requirements.txt
```
#### Set Module
```console
$ pip freeze > requirements.txt 
```

   
### Idea Description
- Matching service to prepare for interviews, studies, and certifications in a short time

## Branch structure

### Main branch
* Master branch : It is Manage only the state that can be distributed
* Develop branch : It is Used to merge branches for feature development

### Secondary branch

* Feature branch : Branch to develop the function ex)feature/profile
* Fix branch : Branch to fix the function ex)fix/profile



## Commit rule
```console
git commit -m "text"
```

|    Keyword    | Description                                        |
| :-----------: | :------------------------------------------------- |
|    [feat]     | 코드나 테스트, 예제, 문서 등의 추가가 있을 때 사용 |
|  [refactor]   | 올바르지 않은 로직을 고친 경우에 사용              |
|    [style]    | 코드에 대한 스타일을 바꿀 때                       |
| [docs(guide)] | 문서 작업을 할 때                                  |

## Convention
#### 1. test.py 작성
- 기능에 대한 validation을 할 수 있는 test code를 작성
- 기능에 대한 문제가 날만한 test code를 작성

#### 2. method
- CRUD 순서로 함수 작성

#### 3. import
- module을 import 해야될 때는 무조건 알파벳 순서로 정리

#### 4. python
- class, function 간의 간격은 무조건 2줄
- class내의 def (method)의 경우에 간격은 무조건 1줄

#### 5. comments
- 로직, class, function에 대한 설명의 주석 작성
- 단 가장 중요한 것은 naming을 잘 지을 것.
- 사용이 안되는 코드의 주석은 무조건 삭제하고 pull request

## Merge Rule
- merge는 확실하게 된 pull request만 할 것
- 에러나 convention이 잘 지켜지지 않았을 경우 코드리뷰를 하거나 보고 수정을 할 것 

