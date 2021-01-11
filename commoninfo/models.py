from django.db import models

# Create your models here.
class Patient(models.Model): 
    unique_ID = models.CharField(max_length=20, unique=True, primary_key = True, help_text="Enter the patient's unique ID: ")
    first_Name = models.CharField(max_length=20, help_text="Enter the patient's first name: ")
    last_Name = models.CharField(max_length=20, help_text="Enter the patient's last name: ")
    date_of_birth = models.DateField(help_text="Enter the patient's date of birth: ")
    address = models.CharField(max_length=40, help_text = 'Enter address of residence')
    phone = models.PositiveIntegerField(max_length = 10, help_text="Enter the patient's phone number")
    email = models.CharField(max_length = 40, help_text = "Enter the patient's email address: ")
    reason_for_visit = models.TextField(max_length = 300, default = 'null', help_text='Enter the reason for visit', )

    class Meta: 
        ordering = ['unique_ID', 'first_Name', 'last_Name', 'date_of_birth', 'address', 'phone', 'email', 'reason_for_visit']

    def get_absolute_url(self): 
        """Returns the url to access a particular instance of Patient"""
        return reverse('patient-detail', args=[str(self.primary_key)])

    def __str__(self): 
        return f'{self.unique_ID}, {self.first_Name}, {self.last_Name}, {self.date_of_birth},{self.address}, {self.phone}, {self.email}, {self.reason_for_visit}'