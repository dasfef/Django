from django.shortcuts import render
from django.http import HttpResponse
from .models import Essay

# Create your views here.
def home (ss) :
    return render(ss, "home.html", {})