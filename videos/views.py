from django.shortcuts import render
from videos.models import Videos, Student
# Create your views here.
def index(request):
    videos = Videos.objects.all()
    students = Student.objects.all()
    context = {
        'videos':videos,
        'students':students,
    }
    return render(request, 'index.html',context)

def about_us(request):
    return render(request, 'about_us.html')