from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@login_required
@csrf_protect
def dashboard(request):
    allow_email = ['dubeysaksham796@gmail.com','dubeysaksham801@gmail.com','singhnidhi2713@gmail.com']

    return render(request, 'dash.html',{'allow_email':allow_email})

@csrf_protect
def logout1(request):
    logout(request)
    return render(request,'logout.html')
