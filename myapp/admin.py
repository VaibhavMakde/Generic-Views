from django.contrib import admin

from myapp.models import Grade, Student, Employee


# Register your models here.
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'mark']



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'graduated', 'grades']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']