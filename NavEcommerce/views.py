from django.shortcuts import render

from django.http import HttpResponse

def Main(request):
    return render(request, 'FirstPage.html')