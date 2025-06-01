from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@login_required
@csrf_protect
def dashboard(request):

    return render(request, 'dash.html')

@csrf_protect
def logout1(request):
    logout(request)
    return render(request,'logout.html')
