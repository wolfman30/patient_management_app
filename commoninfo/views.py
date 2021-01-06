from django.shortcuts import render
from commoninfo.models import Patient

# Create your views here.
def index(request):
    num_patients = Patient.objects.all().count()

    context = {
        'num_patients': num_patients,
    }

    return render(request, 'index.html', context=context)