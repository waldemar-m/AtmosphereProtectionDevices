from django import forms
from .models import Odbiorca
from .models import Parametry
from .models import UOAP0
from .models import UOAP2

class OdbiorcaForm(forms.ModelForm):
   
    class Meta:
        model=Odbiorca
        field='__all__'
        exclude = ()

class ParametryForm(forms.ModelForm):
       
     class Meta:
       model=Parametry
       field='__all__'
       exclude = ()

class UOAP0Form(forms.ModelForm):
     
     class Meta:
         model=UOAP0
         exclude = ()

class UOAP2Form(forms.ModelForm):
     
    class Meta:
        model=UOAP2     
        exclude = ()