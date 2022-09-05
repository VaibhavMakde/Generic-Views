from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from myapp.forms import ContactForm
from myapp.models import Student, Employee


# List View refers to a view (logic)
# to display multiple instances of a table in the database.
class StudentListView(ListView):
    model = Student
    template_name = 'myapp/student.html'
    # custom context name--> default =student_list
    context_object_name = 'students'
    ordering = ['name']

    # filter method for listView

    # Get the list of items for this view.This must be an
    # iterable and may be a queryset
    # ( in which queryset-specific behavior will be enabled).
    def get_queryset(self):
        return Student.objects.filter(graduated=True)

    # Returns context data for displaying the list of objects.

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['defaulter'] = Student.objects.all().order_by('name')
        return context

    # def get_template_names(self):
    #     if self.request.user.is_superuser:
    #         template_name = 'app/superuser.html'
    #     elif self.request.user.is_staff:
    #         template_name = 'app/staff.html'
    #     else:
    #         template_name = self.template_name
    #     return [template_name]


class StudentDetailView(DetailView):
    model = Student
    # by default template = student_detail
    template_name = 'myapp/studentDetail.html'
    # if we want <int:id>
    # pk_url_kwarg = 'id'


class ContactFormView(FormView):
    template_name = 'myapp/student_form.html'
    form_class = ContactForm
    success_url = '/registered_user/'


class Registered_user(TemplateView):
    template_name = 'myapp/registered_successful.html'


class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['name', 'email', 'password']
    success_url = '/registered_user/'


# UpdateView refers to a view (logic) to update a particular
# instance of a table from the database with some extra details.
class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['name', 'email', 'password']
    success_url = '/registered_user/'


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '/employee_create_form/'
