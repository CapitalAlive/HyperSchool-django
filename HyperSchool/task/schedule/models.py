from django.db import models
from django.shortcuts import reverse


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    about = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.surname}"

    def get_absolute_url(self):
        return reverse('teacher_url', kwargs={'pk': self.pk})


class Course(models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField(max_length=1000)
    duration_months = models.IntegerField()
    price = models.IntegerField()
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('courses_url', kwargs={'pk': self.pk})


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.name} {self.surname}"

