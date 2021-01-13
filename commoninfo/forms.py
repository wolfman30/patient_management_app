from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Patient
import datetime




class AddPatient(forms.ModelForm):

    class Meta: 

        model = Patient

        fields = ['unique_ID', 'first_Name', 'last_Name', 'date_of_birth', 'address', 'phone', 'email','reason_for_visit']
        labels = {'unique_ID': 'Unique ID', 'first_Name':'First Name', 'last_name': 'Last Name', 
                    'date_of_birth': 'Date of Birth', 'address': 'Address', 'phone': 'Phone number', 
                    'email': 'Email', 'reason_for_visit': 'Reason for Visit'}

        def validate_dob(self):
            #runs standard clean method 
            cleaned_data = super(AddPatient, self).clean()

            #gets cleaned data from date_of_birth field
            date_of_birth = cleaned_data.get('date_of_birth')

            


            
    


