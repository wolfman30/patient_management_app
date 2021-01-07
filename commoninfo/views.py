from django.shortcuts import render
from commoninfo.models import Patient

# Create your views here.
def index(request):
    num_patients = Patient.objects.all().count()

    context = {
        'num_patients': num_patients,
    }

    return render(request, 'index.html', context=context)

def add_patient(request):
    patient_model = get_object_or_404(Patient)

    #if a post request
    if request.method == 'POST':

        form = AddPatient(request.POST)

    
    #if a get request
    else: 
        pass