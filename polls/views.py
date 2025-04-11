from django.http import HttpResponse # type: ignore

def index(request):
    return HttpResponse("¡Estás viendo el índice de encuestas!")

def detail(request, question_id):
    return HttpResponse(f"Estás viendo la pregunta número {question_id}.")

def results(request, question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"Estás votando en la pregunta {question_id}.")
