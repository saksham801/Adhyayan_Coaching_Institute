from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
@login_required
def dashboard(request):

    return render(request, 'dash.html')

def logout1(request):
    logout(request)
    return render(request,'logout.html')
