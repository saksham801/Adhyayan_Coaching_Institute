from django.shortcuts import render

from home.models import PopularCourse,Toppers


# Create your views here.
def Home(request):
    courses = PopularCourse.objects.all()
    toppers = Toppers.objects.all()
    return render(request,'index.html',{'courses':courses,'toppers':toppers})
