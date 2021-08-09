from django.shortcuts import render
from django.http import HttpResponse
tasks = ['html', 'css', 'python', 'git','Django']
# Create your views here.
def index(request):
    return render(request, 'wikipedia/index.html',{
        'tasks': tasks
    })
def css(request):
    return render(request, 'wikipedia/css.html')
def html(request):
    return render(request, 'wikipedia/html.html')
def git(request):
    return render(request, 'wikipedia/git.html')
def python(request):
    return render(request, 'wikipedia/python.html')
def Django(request):
    return render(request, 'wikipedia/Django.html')
