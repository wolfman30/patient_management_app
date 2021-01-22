from django.db import models
#the use of RegexValidator drawn from 
#https://stackoverflow.com/questions/17165147/how-can-i-make-a-django-form-field-contain-only-alphanumeric-characters
from django.core.validators import RegexValidator

#code from https://stackoverflow.com/questions/5013041/how-to-restrict-user-to-select-date-between-range-of-years-in-django by Ori
from django.core.exceptions import ValidationError 

alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed in names.')
nums = RegexValidator(r'^[0-9]*$', 'Phone number should have only numbers.')
#created the above variable based on Stack Overflow author Martijn Pieters from the URL below
#https://stackoverflow.com/questions/17165147/how-can-i-make-a-django-form-field-contain-only-alphanumeric-characters


def validate_birthyear(value):
    '''
    code from https://stackoverflow.com/questions/5013041/how-to-restrict-user-to-select-date-between-range-of-years-in-django by Ori
    '''
    if value.year < 1910 or value.year > 2021: 
        raise ValidationError(f'{value.year} is not a valid birth year!')

class Patient(models.Model): 
    unique_ID = models.CharField(max_length=20, unique=True, primary_key = True, help_text="Enter the patient's unique ID: ")
    first_Name = models.CharField(max_length=20, validators=[alpha], help_text="Enter the patient's first name: ")
    last_Name = models.CharField(max_length=20, validators=[alpha], help_text="Enter the patient's last name: ")
    date_of_birth = models.DateField(validators=[validate_birthyear], help_text="Enter the patient's date of birth in the form of year-month-day")
    address = models.CharField(max_length=40, help_text = 'Enter address of residence')
    phone = models.CharField(max_length = 12, validators=[nums], help_text="Enter the patient's phone number")
    email = models.EmailField(max_length = 40, blank='True', help_text = "Enter the patient's email address: ")
    reason_for_visit = models.TextField(max_length = 300, help_text='Enter the reason for visit', )

    class Meta: 
        ordering = ['unique_ID', 'first_Name', 'last_Name', 'date_of_birth', 'address', 'phone', 'email', 'reason_for_visit']

    def get_absolute_url(self): 
        """Returns the url to access a particular instance of Patient"""
        return reverse('patient-detail', args=[str(self.primary_key)])

    def __str__(self): 
        return f'{self.unique_ID}, {self.first_Name} {self.last_Name}, {self.date_of_birth},{self.address}, {self.phone}, {self.email}, {self.reason_for_visit}'