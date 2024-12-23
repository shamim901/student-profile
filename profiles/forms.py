from django import forms
from .models import University

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name', 'location', 'established_year', 'website']