from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from .models import BugReport, FeatureRequest
from django.views.generic import ListView, DetailView
'''
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
'''

class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list_url = reverse('quality_control:bugs_page')
        feature_list_url = reverse('quality_control:features_page')
        html = (f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br/>"
                f"<a href='{feature_list_url}'>Запросы на улучшение</a>")
        return HttpResponse(html)

def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список багов</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</br> Status: {bug.status}</a></li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    def get(self, request, *args, **kwargs):
        bug = self.get_object()
        response_html = (f'<h1>{bug.title}</h1><p>Description: {bug.description}</p>'
                         f'<p>Priority: {bug.priority}</p><p>Related project: {bug.project.name}</p>'
                         f'<p>Related task: {bug.task.name}</p>')
        return HttpResponse(response_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</br> Status: {feature.status}</a></li>'
    features_html += '</ul>'
    return HttpResponse(features_html)

class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    def get(self, request, *args, **kwargs):
        feature = self.get_object()
        response_html = (f'<h1>{feature.title}</h1><p>Description: {feature.description}</p>'
                         f'<p>Priority: {feature.priority}</p><p>Related project: {feature.project.name}</p>'
                         f'<p>Related task: {feature.task.name}</p>')
        return HttpResponse(response_html)
