from django import forms
from .models import Patient




class AddPatient(forms.ModelForm):

    class Meta: 

        model = Patient

        fields = ['unique_ID', 'first_Name', 'last_Name', 'date_of_birth', 'address', 'phone', 'email','reason_for_visit']
        labels = {'unique_ID': 'Unique ID', 'first_Name':'First Name', 'last_name': 'Last Name', 
                    'date_of_birth': 'Date of Birth', 'address': 'Address', 'phone': 'Phone number', 
                    'email': 'Email', 'reason_for_visit': 'Reason for Visit'}

        def validate_dob(self):
            pass
    


