from django.shortcuts import render

# Create your views here.

def equipement(request):
    return render(request,'equipement.html')