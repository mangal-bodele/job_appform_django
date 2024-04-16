from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

        labels={
            'dob':"Date Of Birth"
        }