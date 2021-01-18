from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Patient
import datetime
import string


NUMS_sCHARS = "0123456789" + string.punctuation
LETTERS_sCHARS = string.ascii_letters + string.punctuation

class AddPatient(forms.ModelForm):

    class Meta: 

        model = Patient

        fields = ['unique_ID', 'first_Name', 'last_Name', 'date_of_birth', 'address', 'phone', 'email','reason_for_visit']
        labels = {'unique_ID': 'Unique ID', 'first_Name':'First Name', 'last_name': 'Last Name', 
                    'date_of_birth': 'Date of Birth', 'address': 'Address', 'phone': 'Phone number', 
                    'email': 'Email', 'reason_for_visit': 'Reason for Visit'}

    #runs standard clean method
    def cleaned_data(self):
        cleaned_data = super(AddPatient, self).clean()
        return cleaned_data

    def invalid_dob(self):

        '''
        used to validate the birth date: returns true if birth day is in the future or older than 130 years
        '''

        #gets cleaned data from date_of_birth field
        date_of_birth = AddPatient.cleaned_data(self).get('date_of_birth')

        #checks if birth date is in the future 
        if date_of_birth > datetime.date.today():
            return True

        #checks if the person is 130 years old or older
        elif date_of_birth.year < datetime.date.today().year - 130: 
            return True

        return False

    def invalid_fname(self):

        first_name = AddPatient.cleaned_data(self).get('first_Name')

        for letter in first_name: 
            if letter in NUMS_sCHARS: 
                return True

        return False

    def invalid_lname(self): 
        
        last_name = AddPatient.cleaned_data(self).get('last_Name')

        for letter in last_name:
            if letter in NUMS_sCHARS:
                return True
        
        return False

    def invalid_phone(self): 

        phone = AddPatient.cleaned_data(self).get('phone')

        for num in phone: 
            if num in LETTERS_sCHARS:
                return True

        return False 


        

            


            
    


