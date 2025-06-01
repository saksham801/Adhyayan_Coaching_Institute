from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


# Create your views here.


@csrf_protect
def about(request):
    return render(request,'about.html')
