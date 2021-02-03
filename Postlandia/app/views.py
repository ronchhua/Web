from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'html/index.html')


def login(request):

    return render(request, 'html/auth.html')