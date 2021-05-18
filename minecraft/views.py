from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, "minecraft/index.html")