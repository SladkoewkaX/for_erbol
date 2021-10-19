from django import forms
from django.db.models import fields
from .models import Registration
from for_t import models

class RegForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('name', 'surname')