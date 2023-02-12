from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def eggs(request):
    return HttpResponse('<h1>EGGS</h1>')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist)})

def about(request):
    return render(request, 'about.html')