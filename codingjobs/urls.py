from django.contrib import admin
from django.urls import path
from django.contrib.auth import views

from apps.views import homepage, signup
from job.views import job_details
from userprofile.views import dashboard

urlpatterns = [
    path("", homepage, name="homepage"),
    path("signup/", signup, name="signup"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("login/", views.LoginView.as_view(template_name='login.html'), name="login"),
    path("admin/", admin.site.urls),

    path('dashboard/', dashboard, name='dashboard'),

    path('jobs/<int:job_id>/', job_details, name='job_details'),
]
