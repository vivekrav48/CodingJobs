from django.shortcuts import render
from .models import Job

# Create your views here.

def job_details(request, job_id):
    job =  Job.objects.get(pk=job_id)

    return render(request,'job_details.html',{'job':job})


