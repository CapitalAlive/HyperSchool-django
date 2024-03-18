from django.contrib import admin
from . import models
# Register your models here.

for model in [models.Teacher, models.Course, models.Student]:
    admin.site.register(model)