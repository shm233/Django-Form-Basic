from django.shortcuts import render, redirect
from django.contrib import messages
from newapp.models import *
from newapp.forms import *


def student_list(request):
    student = StudentModel.objects.all()
    context = {
        'student' : student
    }
    return render(request, 'students.html', context)

def add_student(request):
    if request.method == 'POST':
        form_student = StudentForm(request.POST, request.FILES)
        if form_student.is_valid():
            form_student.save()
            messages.success(request, "Student Info Added Successfully")
            return redirect('student_list')
    else:
        form_student = StudentForm()
    context = {
        'form_student' : form_student
    }
    return render(request, 'add-student.html', context)

def update_student(request, s_id):
    student = StudentModel.objects.get(id = s_id)
    if request.method == 'POST':
        form_student = StudentForm(request.POST, request.FILES, instance = student)
        if form_student.is_valid():
            form_student.save()
            messages.success(request, "Student Info Updated Successfully")
            return redirect('student_list')
    else:
        form_student = StudentForm(instance = student)
    context = {
        'student' : student,
        'form_student' : form_student
        }
    return render(request, 'update-student.html', context)

def delete_student(request, s_id):
    StudentModel.objects.get(id = s_id).delete()
    return redirect('student_list')
