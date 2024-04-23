from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.shortcuts import get_object_or_404
from .models import BugReport, FeatureRequest
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect
from .forms import BugReportForm, FeatureRequestForm
from django.views.generic.edit import UpdateView, DeleteView


#CREATE FBV
def add_bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.save()
            return redirect('quality_control:bugs_page')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def add_feature_request(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.save()
            return redirect('quality_control:features_page')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

#CREATE CBV
class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:bugs_page')

class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = ('quality_control/feature_request_form.html')
    success_url = reverse_lazy('quality_control:features_page')

#READ FBV
def index(request):
    return render(request, 'quality_control/index.html')

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})


def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})



#READ CBV
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')

class BugListView(ListView):
    model = BugReport
    template_name = 'quality_control/bug_list.html'
    context_object_name = ('bug_list')

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'
    context_object_name = 'bug'

class FeatureListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/feature_list.html'
    context_object_name = 'feature_list'

class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'
    context_object_name = 'feature'

#UPDATE FBV
def update_bug_report(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.save()
            return redirect('quality_control:bugs_page')
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_report_update.html', {'form': form, 'bug': bug})

def update_feature_request(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.save()
            return redirect('quality_control:features_page')
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_request_update.html', {'form': form, 'feature': feature})


#UPDATE CBV
class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_update.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bugs_page')

class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_update.html'
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:features_page')


#DELETE FBV
def delete_bug_report(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bugs_page')

def delete_feature_request(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect('quality_control:features_page')

#DELETE CBV
class BugReportDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    context_object_name = 'bug'
    success_url = reverse_lazy('quality_control:bugs_page')
    template_name = 'quality_control/bug_report_confirm_delete.html'

class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    context_object_name = 'feature'
    success_url = reverse_lazy('quality_control:features_page')
    template_name = 'quality_control/feature_request_confirm_delete.html'















