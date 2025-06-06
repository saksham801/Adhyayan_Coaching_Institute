from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from home.models import Course
from database.course import course_name
import pymongo
from database.course import course_name as cs


client = pymongo.MongoClient('mongodb+srv://dubeysaksham796:Iron_Man@adhyayancoachinginstitu.hqcuhrf.mongodb.net/?retryWrites=true&w=majority&appName=AdhyayanCoachingInstitute')
db = client['Adhyayan_Coaching_Institute']
collection = db['course']



# Create your views here.
@csrf_protect
@login_required

def index(request):


        email = request.user.email
        allow_email = ['dubeysaksham796@gmail.com']
        courses = Course.objects.all()
        user =list( collection.find())

        if request.method == "POST":
            name = request.POST['course_name']
            des = request.POST['course_des']
            link = request.POST['course_url']
            course_name(name = name,des = des,url = link)
            return redirect('suc')



        return render(request,'courses.html',{'user':user,'email':email,'allow_email':allow_email})

