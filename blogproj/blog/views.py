from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse("<h1>Hello everyone and welcome to our django page</h1>")


def casual_page(request):
    return HttpResponse("<h1> This is where happens the next level affairs</h1>")
