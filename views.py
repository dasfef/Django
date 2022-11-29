from django.shortcuts import render
from django.http import HttpResponse
from .models import Ff

# Create your views here.
def home(ss) :
    return render(ss, "Home.html", {})
    # return HttpResponse("<h1>Hello World</>"
    # "<h2>Hello World</>"
    # "<h3>Hello World</>"
    # "<h4>Hello World</>"
    # "<h5>Hello World</>"
    # "<h6>Hello World</>"

def page1(s1) :
    s = Ff.objects.get(f1 = 10001)
    # return render(ss, "Home.html", {})
    return HttpResponse(
    f"<h1><a href = 'http://127.0.0.1:8000/home'>To the Home</a></>"
    "<h2>Hello World</>"
    "<h3>Hello World</>"
    "<h4>Hello World</>"
    "<h5>Hello World</>"
    "<h6>Hello World</>"
    )

def test(s2) :
    return render(s2, "test_game.html", {})