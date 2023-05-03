from django.shortcuts import render
from videos.models import Serial
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