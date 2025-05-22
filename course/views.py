from django.shortcuts import render
from home.models import Course


# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request,'courses.html',{'courses':courses})