from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def contact(requset):
    return render(requset,'contact.html')

def checkout(request):
    return render(request,'checkout.html')
