from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    # return HttpResponse("<h2>This is Pages</h2>")
    return render(request, 'index.html')

def contact(request):
    #return HttpResponse("<h2>about page</h2>")
    return render(request, 'contact.html')

# @login_required(login_url='/admin')
def trainer(request):
    return render(request, 'trainer.html')

def why(request):
    return render(request, 'why.html')
