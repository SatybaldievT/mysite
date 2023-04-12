from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mem/', views.mem, name='mem'),
    path('hot/', views.hot, name='hot'),
    path('best/', views.best, name='best'),
    path('logout/', views.logout, name='logout'),
    path('setting/', views.settings, name='settings'),
    path('tag/<str:tag_name>/', views.tag, name='tag'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('ask/', views.ask, name='ask'),
]

    

