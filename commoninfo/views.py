from django.shortcuts import render
from django.contrib import messages
from .models import Patient
from .forms import AddPatient

# Create your views here.
def index(request):

    return render(request, 'index.html')


def add_patient(request):

    form = AddPatient()

    if request.method == 'POST':
        form = AddPatient(request.POST)
        if form.is_valid():

            if form.invalid_dob(): 
                messages.error(request, 'Invalid date of birth')

            if form.invalid_fname():
                messages.error(request, 'Invalid first name. Names do not have numbers or special characters.')

            if form.invalid_lname():
                messages.error(request, 'Invalid last name. Names do not have numbers or special characters.')

            if form.invalid_phone():
                messages.error(request, 'Invalid phone number. Only use numbers from 0 to 9 without spaces.')

            if True not in [form.invalid_dob(), form.invalid_fname(), form.invalid_lname(), form.invalid_phone()]: 
                form.save()

                messages.success(request, 'Successfully added patient!')
                
                #clears the form for a new entry
                form = AddPatient()

        #else:
            #form = AddPatient()

    return render(request, 'add.html', {'form': form})


def fetch_patient(request):
    
    context = {}
    
    if request.method == 'GET':
        
        try: 
            fetch = Patient.objects.filter(pk=list(request.GET.values())[0])
            
            context = {'fetch': fetch}

        except Exception as e: 
            print(e)
       
        return render(request, 'fetch.html', context)

    
    return render(request, 'fetch.html')