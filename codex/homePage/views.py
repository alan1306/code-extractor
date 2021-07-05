from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Images
from .utils import getFiltered
import base64
from django.core.files.base import ContentFile
import json
from django.core import serializers
def home(request):
    global result
    if request.method=="GET":
        return render(request,'homePage/index.html')
    else:
        image=request.POST.get("image")
        format, imgstr = image.split(';base64,')
        print("format", format)
        ext = format.split('/')[-1]
        file_name = "'myphoto." + ext
        data1 = ContentFile(base64.b64decode(imgstr),name='temp.'+ext)
        data=Images(image=data1)
        data.save()
        results=getFiltered(data.image)
        # print(results)
        if results!="":
            # data=json.dumps(results)
            # print(data)
            # print(results)
            # data=serializers.serialize('json',[data])
            return JsonResponse(results,safe=False)
def result(request):
    return render(request,'homePage/result.html')
    