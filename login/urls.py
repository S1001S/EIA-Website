from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Login Page"),
    path('police_signup/', views.police_signup, name="Police Signup"),
    path('police_login/', views.police_login, name="Police Login"),
    path('citizen_register/', views.citizen_register, name="Citizen Register"),
    path('citizen_login/', views.citizen_login, name="Citizen Login"),
    path('add_criminals/', views.add_criminals, name="Add Criminals"),
    path('detect_criminal/', views.detect_criminal, name="Detect Criminal"),
    path('detect_criminal_video/', views.detect_criminal_video, name="Detect Criminal Video"),
    path('missing_detect/', views.missing_detect, name="Detect Missing"),
    path('file_report/', views.file_report, name="File Report"),
    # path('search_report/', views.search_report, name="Search Reports"),
    path('update_report/', views.update_report, name="Update Reports"),
    # path('search_criminal/', views.search_criminal, name="Search Criminal"),
    path('update_criminal/', views.update_criminal, name="Update Criminal"),
    path('allreports/', views.allreports, name="All Reports"),
    path('allcriminals/', views.allcriminals, name="All Criminals"),
    path('criminalView/<int:pr_id>', views.criminalView, name="Criminal View"),
    path('reportView/<int:pr_id>', views.reportView, name="Report View"),
    path('add_missing/', views.add_missing, name="Add Missing"),
    path('allmissing/', views.allmissing, name="All Missing"),
    # path('search_missing/', views.search_missing, name="Search Missing"),
    path('missingView/<int:pr_id>', views.missingView, name="Missing View"),
    path('track_status/', views.track_status, name="Track Status"),
    path('logout/', views.handlelogout, name="Logout"),
]
