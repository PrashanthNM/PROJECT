from django.shortcuts import render
from django.http import HttpResponse
from .models import Attendence
import psycopg2




# Create your views here.
def index(request):
    return render(request,'index.html')

def student(request):
    return render(request,'student.html')

def students_attendence(request):
    # conn=psycopg2.connect("dbname='telusko' user='postgres' password='prashanth@123' host='localhost' port ='5432' ")
    # cur=conn.cursor()
    # cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER,price REAL)")
    # cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" %("apple",100,100))
    # cur.execute("SELECT * FROM store")
    # rows=cur.fetchall()
    # conn.commit()
    # conn.close()
    
    attendence = Attendence.objects.all() #this error can be ignored



    return render(request,'students_attendence.html',{'attendence':attendence})

def students_marks(request):
    return render(request,'students_marks.html')

def teacher_marks(request):
    return render(request,'teacher_marks.html')

def teacher_update_attendence(request):
    return render(request,'teacher_update_attendence.html')

def teacher(request):
    return render(request,'teacher.html')


