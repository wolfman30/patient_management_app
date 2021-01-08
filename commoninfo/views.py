from django.shortcuts import render
from commoninfo.models import Patient

# Create your views here.
def index(request):

    return render(request, 'index.html')

def add_patient(request):
    #patient_model = get_object_or_404(Patient)

    return render(request, 'add.html')