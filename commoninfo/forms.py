from django import forms 
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class AddPatient(forms.Form):
    unique_ID = forms.CharField(max_length=20, unique=True, primary_key = True, help_text="Enter the patient's unique ID: ")
    first_Name = forms.CharField(max_length=20, help_text="Enter the patient's first name: ")
    last_Name = forms.CharField(max_length=20, help_text="Enter the patient's last name: ")
    date_of_birth = forms.DateField(help_text="Enter the patient's date of birth: ")

    def clean_dob(self): 
        data = self.cleaned_data['date_of_birth']
