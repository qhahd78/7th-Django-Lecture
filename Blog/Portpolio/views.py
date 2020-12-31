from django.shortcuts import render

# Create your views here.


def portpolio(request):
    return render(request, 'portpolio.html')
