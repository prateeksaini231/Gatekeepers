from django.shortcuts import render
from .models import Visitors
from django.urls import reverse
from datetime import date, datetime
from django.http import JsonResponse, HttpResponseRedirect, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder

# Landing Page
def home(request):
    return render(request, 'keeper/home.html')

# Visitor Entry form
def register_page(request):
    return render(request, 'keeper/register.html')

# Find by House number
def find_page(request):
    return render(request, 'keeper/find.html')

# Updata database endpoint
@csrf_exempt
def guards(request):
    v = Visitors(name=request.POST['name'], purpose = request.POST['purpose'].lower(), houseno =  request.POST['houseno'].replace('-', '').upper())
    v.date_time = datetime.now()
    v.save()
    return HttpResponseRedirect(reverse('keeper:home'))

# Read database endpoint
def residents(request):
    try:
        visits = Visitors.objects.filter(houseno = request.GET['houseno'].replace('-', '').upper())
    except Visitors.DoesNotExist:
        raise Http404("No Visitors Found visiting said house")
    return render(request, 'keeper/list.html', {'visits' : visits})
