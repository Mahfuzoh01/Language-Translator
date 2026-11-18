from django.shortcuts import render

def home(request):
    return render(request, 'TransApp/index.html')
