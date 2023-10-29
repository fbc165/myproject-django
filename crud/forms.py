from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Question

EXAM_CHOICES = [
        ('Cloud Practitioner', 'Cloud Practitioner'),
        ('Data Engineer', 'Data Engineer'),
        ('Data Engineer', 'Data Engineer'),
        ('Data Analytics', 'Data Analytics'),
        ('Data Base', 'Data Base'),
    ]
SUBJECT_CHOICES = [
        ('All', 'All'),
        ('Compute Services', 'Compute Services'),
        ('Storage Services', 'Storage Services'),
        ('Networking', 'Data Engineer'),
        ('Data Analytics', 'Networking'),
        ('Databases', 'Databases'),
        ('Management and Governance', 'Management and Governance'),
        ('AWS Global Infrastructure', 'AWS Global Infrastructure'),
        ('Architectural Best Practices', 'Architectural Best Practices'),
    ]


class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class SearchForm(forms.Form):
    exam = forms.ChoiceField(choices=EXAM_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


class CreateQuestionForm(forms.ModelForm):

    class Meta:
        
        model = Question
        fields = ['title', 'description', 'exam', 'subject', 'answer', 'image']

    exam = forms.ChoiceField(choices=EXAM_CHOICES)
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)


    