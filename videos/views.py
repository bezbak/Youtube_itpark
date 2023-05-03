from django.shortcuts import render
from videos.models import Serial, Season
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