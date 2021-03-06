from django.shortcuts import render
from django.contrib import messages
from .models import Patient
from .forms import AddPatient


def index(request):

    return render(request, 'index.html')


def add_patient(request):
    '''
    renders the form to register a new patient on the html template add.html
    '''

    form = AddPatient()

    if request.method == 'POST':

        form = AddPatient(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, 'Successfully added patient!')
            
            #clears the form for a new entry
            form = AddPatient()

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