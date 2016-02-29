from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .forms import OdbiorcaForm
from .forms import ParametryForm
from .odels import Odbiorca

def widok(request):
    return HttpResponse('To jest test <b>tekst</b>')

def testowywidok(request):
    return render_to_response('test.html')

def mainwebsite(request):    
    form=OdbiorcaForm()
    odbiorc=Odbiorca.objects.all()
    return render_to_response('mainwebsite.html',{'news':odbiorc},{'form':form})

def editProject(request):
    form2=ParametryForm()
    return render(request,'edit.html',{'form':form2})
