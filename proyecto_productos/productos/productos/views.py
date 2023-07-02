from django.http import HttpResponse

def index(request):
    return HttpResponse("Vacío. Dirigete a /productos para la utilizar la única funcionalidad disponible.")