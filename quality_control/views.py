from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from .models import BugReport, FeatureRequest
from django.views.generic import ListView, DetailView
from django.shortcuts import render
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
        return render(request, 'quality_control/index.html')

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        return render(request, 'quality_control/bug_detail.html', {'bug': bug})
def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})

class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        return render(request, 'quality_control/feature_detail.html', {'feature': feature})
