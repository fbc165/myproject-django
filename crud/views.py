from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . forms import CreateUserForm, LoginForm, SearchForm, CreateQuestionForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .models import Question

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@login_required
def myquestions(request):
    questions = Question.objects.filter(creator=request.user)
    return render(request, 'my-questions.html', {'questions': questions})

@login_required
def deletequestion(request, question_id):
    question = get_object_or_404(Question, pk=question_id, creator=request.user)
    if request.method == 'POST':
        question.delete()
    return redirect('my-questions')
    

def homepage(request):
    return render(request, 'home.html')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("my-login")

    context = {'registerform':form}
    return render(request, 'register.html', context=context)

def my_login(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    context = {'loginform':form}

    return render(request, 'my-login.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect("homepage")

@login_required(login_url="my-login")
def addquestion(request):
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.creator = request.user
            question.save()
           # form.save()  # Salva a nova pergunta no banco de dados
            return redirect('my-questions')  # Redireciona para a lista de perguntas (crie a URL correspondente)
    else:
        form = CreateQuestionForm()
    
    return render(request, 'add.html', {'form': form})

@login_required(login_url="my-login")
def dashboard(request):
    form = SearchForm(request.GET)
    questions = []
    exam = None
    subject = None
    users = User.objects.all()
    if form.is_valid():
        exam = form.cleaned_data['exam']
        subject = form.cleaned_data['subject']
        
    if exam and subject:
        questions = Question.objects.filter(exam=exam, subject=subject)
    elif exam:
        questions = Question.objects.filter(exam=exam)
    elif subject:
        questions = Question.objects.filter(subject=subject)

    return render(request, 'dashboard.html', {'form': form, 'questions': questions })
