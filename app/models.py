from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=30)
    student_lastname = models.CharField(max_length=30)
    gpa = models.FloatField()
    
    def __str__(self):
        return self.student_name

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=30)
    teacher_lastname = models.CharField(max_length=30)
    students = models.ManyToManyField(Student, related_name='teachers')

    def __str__(self):
        return self.teacher_name