from django.shortcuts import render
from videos.models import Serial, Season, Series
# Create your views here.
def index(request):
    serial = Serial.objects.all()
    context = {
        'serial':serial
    }
    return render(request, 'home.html',context)

def post_detail(request, id):
    serial=Serial.objects.get(id=id)
    context ={
        'serial':serial
    }
    return render(request, 'video-post.html', context)

def season(request, id):
    season = Season.objects.get(id=id)
    context ={
        'season':season
    }
    return render(request, 'video-seasons-post.html', context)

def series(request, id):
    episode = Series.objects.get(id = id)
    # list_of_students = [
    #     'adilet',
    #     'Abbos',
    #     'Bilal'
    # ]
    context = {
        'episode':episode,
        # 'list_of_students':list_of_students
    }
    return render(request, 'seria.html', context)