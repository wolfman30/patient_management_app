from django import forms 
from .models import Patient


class AddPatient(forms.ModelForm):

    class Meta: 

        model = Patient

        fields = ['unique_ID', 'first_Name', 'last_Name', 'date_of_birth', 'reason_for_visit']
        labels = {'unique_ID': 'Unique ID', 'first_Name':'First Name', 'last_name': 'Last Name', 
                    'date_of_birth': 'Date of Birth', 'reason_for_visit': 'Reason for Visit'}
    
 


