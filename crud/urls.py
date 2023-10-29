from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('register', views.register, name='register'),
    path('my-login', views.my_login, name='my-login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name="logout"),
    path('add', views.addquestion, name="addquestion"),
    path('my-questions', views.myquestions, name="my-questions"),
    path('deletequestion/<int:question_id>/', views.deletequestion, name="deletequestion"),
    path('', views.personal_page, name="personal"),
]
