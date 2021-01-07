from django import forms 

class AddPatient(forms.Form):
    unique_ID = forms.CharField(max_length=20, unique=True, primary_key = True, help_text="Enter the patient's unique ID: ")
    first_Name = forms.CharField(max_length=20, help_text="Enter the patient's first name: ")
    last_Name = forms.CharField(max_length=20, help_text="Enter the patient's last name: ")
    date_of_birth = forms.DateField(help_text="Enter the patient's date of birth: ")
