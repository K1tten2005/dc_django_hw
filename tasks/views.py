from django.http import HttpResponse
from django.urls import reverse

def index(request):
    another_page_url = reverse('tasks:another_page')
    quality_control_page_url = reverse('quality_control:index')
    html = (f"<h1>Страница приложения tasks</h1><a href='{another_page_url}'>Перейти на другую страницу</a><br/>"
            f"<a href='{quality_control_page_url}'>Перейти на страницу приложения quality control</a>")
    return HttpResponse(html)

def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")