from django.shortcuts import render
from django.http import HttpResponse


def home(req):
    return HttpResponse("<h1> Hey Whatsup </h1>")


def about(req):
    return HttpResponse("<h1>About Page </h1>")


# Create your views here.
