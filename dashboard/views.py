from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import make_password,check_password
import pymongo

client = pymongo.MongoClient('mongodb+srv://dubeysaksham796:Iron_Man@adhyayancoachinginstitu.hqcuhrf.mongodb.net/?retryWrites=true&w=majority&appName=AdhyayanCoachingInstitute')
db = client['Adhyayan_Coaching_Institute']
collection1 = db['contact']
collection2 = db['message']


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

@login_required
@csrf_protect
def message(request):
    allow_email = ['dubeysaksham796@gmail.com','dubeysaksham801@gmail.com','singhnidhi2713@gmail.com']
    if request.user.email in allow_email:
        message1 = list(collection1.find())
        message2 = list(collection2.find())
        return render(request,'mess.html',{"message": message1,"message2":message2})
    else:
        return render(request, 'index.html')