from django import forms
from django.forms import ModelForm
from .models import Magazine
class MagazineForm(ModelForm):
    class Meta:
        model = Magazine
        fields = "__all__"