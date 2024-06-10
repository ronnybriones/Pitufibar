from django.shortcuts import render # type: ignore
from django.http import HttpResponse

def home(request):
<<<<<<< HEAD
    return HttpResponse("hola, esta es la pagina principal")
=======
    return HttpResponse("Hello, world. You're at the home page.")
>>>>>>> origin/master
# Create your views here.
def home (request):
    return render(request, 'home.html')
