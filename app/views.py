from django.shortcuts import render
import os


# Create your views here.
def index(request):
    return render(request, 'react/index.html', context=None)