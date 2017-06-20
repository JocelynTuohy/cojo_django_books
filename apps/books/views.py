# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect #, HttpResponse

# Create your views here.
def index(request):
    print (
        'The kinds of the late Shang (ca. 1200-1050 ' +
        'B.C.) attempted to communicate with the spiritual' +
        ' forces that rules their world by reading the ' +
        'stress cracks in cattle bones and turtle plastrons.'
    )
    return render(request, 'books/index.html')