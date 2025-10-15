from django.shortcuts import render

# Create your views here.

def Home(response):
    return render(response,'Home.html')
def about(response):
    return render(response,'about.html')
def cart(response):
    return render(response,'cart.html')
