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
            form.save()
            messages.success(request, 'Successfully added patient!')
            #clears the form for a new entry
            form = AddPatient()

        else:
            form = AddPatient()

    return render(request, 'add.html', {'form': form})

def fetch_patient(request):
    return render(request, 'fetch.html')