
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.StudentListView.as_view(), name="student"),
    path('student_detail/<int:pk>', views.StudentDetailView.as_view(), name="student_detail"),
    path('contact_form/', views.ContactFormView.as_view(), name="contact_form"),
    path('registered_user/', views.Registered_user.as_view(), name="registered_user"),
    path('employee_create_form/', views.EmployeeCreateView.as_view(), name="employeeCreateView"),
    path('employee_update_form/<int:pk>', views.EmployeeUpdateView.as_view(), name="employeeUpdateView"),
    path('employee_delete/<int:pk>', views.EmployeeDeleteView.as_view(), name="employeeDeleteView"),
]
