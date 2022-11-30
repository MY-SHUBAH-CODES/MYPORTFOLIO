from django.shortcuts import render
from app1.models import *

# Create your views here.
def home(request):
    files=MyCirtificates.objects.get(id=1)
    file=files.mycv
    url=file.url
    return render(request,'index.html',{'url':url})
