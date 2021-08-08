from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('css', views.css, name= 'css'),
    path('html', views.html, name= 'html'),
    path('git', views.git, name= 'git'),
    path('python', views.python, name= 'python'),
    path('Django', views.Django, name= 'Django'),
]