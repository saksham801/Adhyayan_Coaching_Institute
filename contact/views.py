import time

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from contact.models import Contact
from database.contact import contact_data


# Create your views here.
@csrf_protect
def contact1(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        no = request.POST['phone']
        contact_data(name = name,email = email,phone_no = no,message = message,)
        return redirect('suc')


    return render(request,'cont.html')


