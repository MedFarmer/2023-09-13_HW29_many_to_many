from django.contrib import admin
from django.urls import path
from app.views import StudentView, TeacherView, StudentCreate, TeacherCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentView.as_view(), name='students'),
    path('teachers/', TeacherView.as_view(), name='teachers'),
    path('student_create/', StudentCreate.as_view(), name='studentcreate'),
    path('teacher_create/', TeacherCreate.as_view(), name='teachercreate'),
]
