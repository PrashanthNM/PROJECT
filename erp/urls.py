from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[

    path('',views.index,name="home"),
    path('student.html',views.student,name="student"),
    path('students_attendence.html',views.students_attendence,name="students_attendence"),
    path('students_marks.html',views.students_marks,name="students_marks"),
    path('teacher_marks.html',views.teacher_marks,name="teacher_marks"),
    path('teacher_update_attendence.html',views.teacher_update_attendence,name="teacher_update_attendence"),
    path('teacher.html',views.teacher,name="teacher"),
    #path('accounts/',include('accounts.urls')
]