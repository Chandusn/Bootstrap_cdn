from django.shortcuts import render

# Create your views here.
def bootstrap_cdn(request):
    return render(request,'bootstrap_cdn.html')

def first(request):
    return render(request,'first.html')

def home(request):
    return render(request,'home.html')
