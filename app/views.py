from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView
from django.forms import ModelForm
from django.urls import reverse_lazy

class StudentView(ListView):
    model = Student
    template_name = 'students.html'
    context_object_name = 'students'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('student_name', 'student_lastname', 'gpa')

class StudentCreate(CreateView):
    form_class = StudentForm
    template_name = 'studentcreate.html'
    success_url = reverse_lazy('students')    

class TeacherView(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers'

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('teacher_name', 'teacher_lastname', 'students')

class TeacherCreate(CreateView):
    form_class = TeacherForm
    template_name = 'teachercreate.html'
    success_url = reverse_lazy('teachers')  