from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect

import home,time
from home.models import PopularCourse,Toppers,Newsettleer
from database.message import message_data



# Create your views here.
@csrf_protect
def Home(request):
    courses = PopularCourse.objects.all()
    toppers = Toppers.objects.all()

    if request.method == "POST":
        name = request.POST['names']
        email = request.POST['emails']
        message = request.POST['message1']
        message_data(name = name,email = email,message = message)
        return redirect(success)













    return render(request,'index.html',{'courses':courses,'toppers':toppers})

def success(request):
    return render(request,'success.html')