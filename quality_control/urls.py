from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    #CREATE FBV
    path('bugs/new/', views.add_bug_report, name='create_bug_report'),
    path('features/new/', views.add_feature_request, name='create_feature_request'),

    #CREATE CBV
    path('bugs/new/', views.BugReportCreateView.as_view(), name='create_bug_report'),
    path('features/new/', views.FeatureRequestCreateView.as_view(), name='create_feature_request'),


    #READ FBV
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bugs_page'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail_page'),
    path('features/', views.feature_list, name='features_page'),
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail_page'),

    #READ CBV
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugListView.as_view(), name='bugs_page'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail_page'),
    path('features/', views.FeatureListView.as_view(), name='features_page'),
    path('features/<int:feature_id>/', views.FeatureRequestDetailView.as_view(), name='feature_detail_page'),


    #UPDATE FBV
    path('bugs/<int:bug_id>/update', views.update_bug_report, name='update_bug_report'),
    path('features/<int:feature_id>/update', views.update_feature_request, name='update_feature_request'),

    #UPDATE CBV
    path('bugs/<int:bug_id>/update', views.BugReportUpdateView.as_view(), name='update_bug_report'),
    path('features/<int:feature_id>/update', views.FeatureRequestUpdateView.as_view(), name='update_feature_request'),


    #DELETE FBV
    path('bugs/<int:bug_id>/delete', views.delete_bug_report, name='delete_bug_report'),
    path('features/<int:feature_id>/delete', views.delete_feature_request, name='delete_feature_request'),

    #DELETE FBV
    #path('bugs/<int:bug_id>/delete', views.BugReportDeleteView.as_view(), name='delete_bug_report'),
    #path('features/<int:feature_id>/delete', views.FeatureRequestDeleteView.as_view(), name='delete_feature_request'),
]