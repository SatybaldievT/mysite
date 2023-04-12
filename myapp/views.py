import json
import random
from django.shortcuts import render
from .models import Question, Answer, Tag,UserProfile
from django.shortcuts import redirect
"""
def base(request, question_id):
    return render(request, 'base.html')
"""
def paginate(objects_list, request, per_page= 5):
    # Проверяем корректность параметров пагинации
    if not request:
        raise ValueError("request должен быть объектом запроса (request)")
    if not isinstance(per_page, int) or per_page <= 0:
        raise ValueError("per_page должен быть положительным целым числом")

    # Получаем номер текущей страницы из GET-параметра 'page'
    page = request.GET.get('page')

    # Обработка некорректных значений 'page'
    if not page:
        page = 1
    try:
        page = int(page)
    except ValueError:
        page = 1

    # Проверка на выход за границы количества страниц
    if page < 1:
        page = 1
    elif page > (len(objects_list) + per_page - 1) // per_page:
        page = (len(objects_list) + per_page - 1) // per_page

    # Вычисляем индексы начала и конца списка объектов на текущей странице
    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    # Получаем объект страницы и список объектов на этой странице
    current_page = page
    objects_on_page = objects_list[start_index:end_index]
    ret = {'has_previous': (current_page!=1 ),
        'has_next': (current_page != (len(objects_list) + per_page - 1) // per_page),
        'next_page_number' : page +1,
        'previous_page_number' : page - 1,
        'num_pages': (len(objects_list) + per_page - 1) // per_page,
        'num' : page,
        }

    return  {'paginator': ret, 'questions': objects_on_page} 
    # Возвращаем объект текущей страницы и данные для шаблона пагинатора

def index(request):
    # Получаем значение куки с именем пользователя
    username = request.COOKIES.get('user')

    questions = Question.objects.all()
    buff = paginate(questions, request)
    return render(request, 'index.html', {
        'paginator': buff['paginator'],
        'questions': buff['questions'],
        'user': {
        'name':username,
        'is_authenticated': username == 'admin',
        }})
def best(request):
    # Получаем значение куки с именем пользователя
    username = request.COOKIES.get('user')

    questions = Question.objects.order_by('-rating')
    buff = paginate(questions, request)
    return render(request, 'index.html', {
        'paginator': buff['paginator'],
        'questions': buff['questions'],
        'user': {
        'name':username,
        'is_authenticated': username == 'admin',
        }})
def hot(request):
    tag = Tag.objects.all()[:20]
    return render(request, 'hot.html', {'questions': tag, 'type': 'tag'})
def mem(request):
    user = UserProfile.objects.all()[:20]
    return render(request, 'hot.html', {'questions': user})

def is_tag(x,tag_name):
    for tag in x.tags.all():
        if (tag_name == tag.name):
            return True
    return False

def tag(request, tag_name):
    # Получаем значение куки с именем пользователя
    username = request.COOKIES.get('user')

    questions = Question.objects.filter(tags__name=tag_name)
    buff = paginate(questions, request)
    return render(request, 'index.html', {
        'block_name': "#"+tag_name,
        'paginator': buff['paginator'],
        'questions': buff['questions'],
        'user': {
        'name':username,
        'is_authenticated': username == 'admin',
        }})
def question(request, question_id):
    # Получаем значение куки с именем пользователя
    username = request.COOKIES.get('user')
    question = Question.objects.get(id=question_id)
    answers = Answer.objects.filter(question=question)
    buff = paginate(answers, request)
    return render(request, 'question.html', {
        'paginator': buff['paginator'],
        'answers': buff['questions'],
        'user': {
            'name': username,
            'is_authenticated': username == 'admin',
        }
    })
def add_question(request):
    if request.method == 'POST':
        # Получаем данные формы
        title = request.POST['title']
        text = request.POST['text']
        tags = request.POST['tags'].split(',')
        # Создаем новый объект вопроса и сохраняем его в БД
        question = Question(title=title, text=text, rating=0, views=0)
        question.save()

        # Создаем и сохраняем объекты тегов связанных с вопросом
        for tag_name in tags:
            tag_name = tag_name.strip()
            tag, created = Tag.objects.get_or_create(name=tag_name)
            question.tags.add(tag)

        return redirect('index')

    return render(request, 'question.html')
def ask(request):
    return render(request, 'ask.html')
def upvote(request, question_id):
    question = Question.objects.get(id=question_id)
    question.rating += 1
    question.save()
    return redirect('question_detail', question_id=question_id)

def downvote(request, question_id):
    question = Question.objects.get(id=question_id)
    question.rating -= 1
    question.save()
    return redirect('question_detail', question_id=question_id)

def login(request):
    if request.method == 'POST':
        # Получаем данные формы
        username = request.POST['username']
        password = request.POST['password']
        # Проверяем правильность логина и пароля
        if username == 'admin' and password == 'password':
            response = redirect('index')
            # Устанавливаем куку с именем пользователя
            response.set_cookie('user', username)
            return response
        else:
            # Если логин или пароль неправильные, добавляем сообщение об ошибке
            return render(request, 'registration/login.html' ,{'error_message': 'Неправильный логин или пароль.' })
    
    return render(request, 'registration/login.html')
def logout(request):
    response = redirect('index')
    # Удаляем куку с именем пользователя
    response.delete_cookie('user')
    return response

def settings(request):
    if request.method == 'POST':
        # Получаем данные формы
        username = request.POST['username']
        email = request.POST['email']
        # Сохраняем данные настроек пользователя в базе данных или внешнем источнике
        # ...
        # Добавляем сообщение об успешном сохранении настроек
        messages.success(request, 'Настройки успешно сохранены.')
        # Редиректим пользователя на страницу настроек
        return redirect('settings')
    else:
        # Выводим страницу настроек с текущими данными пользователя
        return render(request, 'registration/settings.html')

def signup(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        email = request.POST.get('email')
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        avatar = request.FILES.get('avatar')

        # Проверка условий на пароль и логин
        if len(login) < 5:
            error_message = 'Login should be at least 5 characters long.'
        elif len(password) < 8:
            error_message = 'Password should be at least 8 characters long.'
        elif password != repeat_password:
            error_message = 'Passwords do not match.'
       
        return render(request, 'registration/register.html', {'error_message': error_message})

    return render(request, 'registration/register.html')
