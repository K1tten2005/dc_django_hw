from django.http import HttpResponse
from django.urls import reverse

def index(request):
    bug_list_url = reverse('quality_control:bugs_page')
    feature_list_url = reverse('quality_control:features_page')
    html = (f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br/>"
            f"<a href='{feature_list_url}'>Запросы на улучшение</a>")
    return HttpResponse(html)

def bug_list(request):
    return HttpResponse(f"<h1>Cписок отчетов об ошибках</h1>")
def feature_list(request):
    return HttpResponse(f"<h1>Список запросов на улучшение</h1>")
def bug_detail(request, bug_id):
    return HttpResponse(f"<h1>Детали бага {bug_id}</h1>")
def feature_id_detail(request, feature_id):
    return HttpResponse(f"<h1>Детали улучшения {feature_id}</h1>")