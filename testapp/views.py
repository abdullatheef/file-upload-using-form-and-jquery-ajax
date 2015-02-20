from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.
import json

@csrf_exempt
def home(request):
    if request.method == 'POST':
        img = request.FILES.get('img1')
        if img:
            destination = open(settings.MEDIA_ROOT+"testapp/"+img.name, 'wb+')
            for chunk in img.chunks():
                destination.write(chunk)
            destination.close()
            print img.content_type
            return render(request, 'testapp/templates/home.html', {'imgurl': img.name, 'type' : img.content_type})
        img = request.FILES.get('img2')
        if img:
            destination = open(settings.MEDIA_ROOT+"testapp/"+img.name, 'wb+')
            for chunk in img.chunks():
                destination.write(chunk)
            destination.close()
            print img.content_type
            return HttpResponse(json.dumps({"response": settings.MEDIA_URL + "testapp/" + img.name, "file_type": img.content_type}))
    return render(request, 'testapp/templates/home.html', {})