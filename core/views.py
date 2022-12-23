from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Image
# Create your views here.

def home(request):
    images=Image.objects.all()
    context={
        'images':images
    }
    return render(request, 'index.html', context)

def file_upload(request):
    if request.method == 'POST':
        my_file=request.FILES.get('file')
        Image.objects.create(image=my_file)
        return HttpResponse('')
    return JsonResponse({'post':'false'})