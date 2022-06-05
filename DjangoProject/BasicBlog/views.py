from django.shortcuts import render
from django.http import HttpResponse


def home(req):
    return HttpResponse("<h1> Hey Whatsup </h1>")


# Create your views here.
