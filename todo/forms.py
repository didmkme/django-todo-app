from django import forms
from django.forms import ModelForm
from .models import Project

class ProjectForm(forms.Form):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(
                                attrs={'class': 'form-control'}
                                )
                            )
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={'cols': "80", 'rows': "10", 'class': 'form-control'}
                                      )
                                )