from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@csrf_protect
@login_required
def ac(request):
    allow = ['dubeysaksham796@gmail.com','dubeysaksham801@gmail.com','singhnidhi2713@gmail.com']
    if request.user.email in allow:

        return render(request,'aci_pan.html')
    else:
        return render(request,'index.html')