from django.shortcuts import render
from .models import Portpolio
# Create your views here.


def portpolio(request):
    portpolios = Portpolio.objects
    return render(request, 'portpolio.html', {'portpolios': portpolios})
