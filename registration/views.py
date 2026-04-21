from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm, CourseForm, CourseReportForm
from .models import Registration


def student_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student registered successfully!')
            return redirect('student_register')
    else:
        form = StudentForm()
    return render(request, 'registration/student_form.html', {'form': form})


def course_register(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student enrolled in course successfully!')
            return redirect('course_register')
    else:
        form = CourseForm()
    return render(request, 'registration/course_form.html', {'form': form})


def course_report(request):
    form = CourseReportForm(request.GET or None)
    students = []
    selected_course = None
    if form.is_valid():
        selected_course = form.cleaned_data['course']
        students = Registration.objects.filter(
            course=selected_course
        ).select_related('student')
    return render(request, 'registration/course_report.html', {
        'form': form,
        'students': students,
        'selected_course': selected_course,
    })
