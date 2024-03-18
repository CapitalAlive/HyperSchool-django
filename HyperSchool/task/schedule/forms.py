from django import forms
from django.forms.models import ModelForm
from . import models


class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=255,
        label="Search",
        widget=forms.TextInput(
            attrs={
                "class": "search",
                "placeholder": ""
            }
        )
    )


class AddCourseForm(ModelForm):
    class Meta:
        model = models.Student
        exclude = []
