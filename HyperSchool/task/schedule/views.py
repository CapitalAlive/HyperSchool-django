from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from . import models
from . import forms
from django.contrib.auth.forms import UserCreationForm



def main(request):
    if request.method == "GET":
        form = forms.SearchForm(request.GET)
    elif request.method == "POST":
        form = forms.SearchForm(request.POST)
    if form.is_valid():
        q = form.cleaned_data["q"]
        objects = models.Course.objects.filter(title__contains=q)
    else:
        objects = models.Course.objects.all()

    context = {"form": form, "objects": objects}
    response = render(request, "schedule/index.html", context=context)
    return response


def course_details(request, pk):
    course = models.Course.objects.filter(pk=pk).first()
    students = models.Student.objects.filter(course=course)
    context = {"course": model_to_dict(course), "students": students}
    return render(request, "schedule/course_details.html", context)


def teacher_details(request, pk):
    teacher = model_to_dict(models.Teacher.objects.filter(pk=pk).first())
    response = render(request, "schedule/teacher_details.html", {"teacher": teacher})
    return response


def add_course(request):
    form = forms.AddCourseForm
    if request.method == "GET":
        return render(request, "schedule/add_course.html", {"form": form})
    elif request.method == "POST":
        form = form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "schedule/add_course.html", {"form": form, "success": True})


def sign_up(request):
    if request.method == "GET":
        return render(request, "schedule/signup.html", {"form": UserCreationForm})
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main")
