from django.shortcuts import render # type: ignore
from django.http import HttpResponse

def home(request):
    return HttpResponse("hola, esta es la pagina principal")
# Create your views here.
def home (request):
    return render(request, 'home.html')