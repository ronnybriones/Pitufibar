from django.shortcuts import render # type: ignore
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the home page.")
# Create your views here.
def home (request):
    return render(request, 'home.html')
