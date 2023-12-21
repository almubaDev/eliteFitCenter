from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def test(request):
    return render(request, 'home/test.html')