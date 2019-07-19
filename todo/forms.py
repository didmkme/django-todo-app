# pylint: disable=no-member
from django import forms
from django.forms import ModelForm
from .models import Project, Issue

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
    class Meta:
        model = Project
        fields = ['title']
                                
class IssueForm(forms.Form):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(
                                attrs={'class': 'form-control'}
                                )
                            )
    open_date = forms.DateTimeField(label='Open Date', 
                                    widget=forms.DateTimeInput(
                                        attrs={'class':'forms-control'}
                                        )
                                )

    close_date = forms.DateTimeField(label='Close Date', 
                                    widget=forms.DateTimeInput(
                                        attrs={'class':'forms-control'}
                                        )
                                )
    class Meta:
        model = Issue
        fields=['title', 'open_date', 'close_date']