"""
URL configuration for payroll_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(r"payroll_tracker/", include("employee.urls")),
    path(r"payroll_tracker/", include("department.urls")),
    path(r"payroll_tracker/", include("designation.urls")),
    path(r"payroll_tracker/", include("leave.urls")),
    path(r"payroll_tracker/", include("reimbursement.urls")),
    path(r"payroll_tracker/", include("attendance.urls")),
    path(r"payroll_tracker/", include("user.urls")),
]
if settings.DEBUG:
    # static url works in development mode so checking debug is true
    urlpatterns += staticfiles_urlpatterns()
