from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def read(request):
    return render(request,'read.html')

def display_json(request):
    return render(request,'display_json.html')