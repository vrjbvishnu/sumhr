from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def current_datetime(request):
    context={}
    template_name = 'company/home.html'
    return render(request, template_name, context)