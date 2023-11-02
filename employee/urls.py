from rest_framework import routers
from employee.admin_views import EmployeeCreateAdminView, EmployeeListAdminView, EmployeeRetrieveAdminView
from django.urls import path, include

admin_router = routers.DefaultRouter()
admin_router.register('admin/employee/create', EmployeeCreateAdminView, 'employee-create')
admin_router.register('admin/employee/list', EmployeeListAdminView, 'employee-list')
admin_router.register('admin/employee/retrieve', EmployeeRetrieveAdminView, 'employee-retrieve')

urlpatterns = [
    path('', include(admin_router.urls)),
]