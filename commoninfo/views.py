from django.shortcuts import render
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
        else:
            form = AddPatient()

    return render(request, 'add.html', {'form': form})

def fetch_patient(request):
    return render(request, 'fetch.html')