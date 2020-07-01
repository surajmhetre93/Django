from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Loginform

# Create your views here.
# def home(request):
#     return HttpResponse("Hello! This is the first page of my app!")

def about(request):
    return HttpResponse("Hello! This is the about-us page of my app!")

def contact(request):
    return HttpResponse("Hello! This is the contact page of my app!")

def home(request):
    return render(request, "myapp/home.html")

def form_view(request):
    if request.method == "POST":
        form = Loginform(request.POST)
        if form.is_valid():
            print("validation worked")
            print("Name", form.cleaned_data['name'])
            print("Email", form.cleaned_data['email'])
            try:
                form.save()
                return redirect("success")
            except Exception as ex:
                print("Error in saving form", ex.message)
            
    else:
        form = Loginform()
    return render(request, "myapp/index.html", {'form':form})

def success(request):
    return render(request, 'myapp/success.html')