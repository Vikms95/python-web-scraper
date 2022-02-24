from django.http import HttpResponse
from django.template import loader
from django.template.context import Context

def test(request):

    ctx = {}
    documento_plantillas = loader.get_template('plantillapadre.html')
    plantilla = documento_plantillas.render(ctx)
    return HttpResponse(plantilla)

def actor_of_the_day(request):
    ctx = {}
    documento_plantillas = loader.get_template("plantillaactoroftheday.html")
    plantilla = documento_plantillas.render(ctx)
    return HttpResponse(plantilla)
