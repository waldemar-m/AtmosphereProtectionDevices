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
<<<<<<< HEAD
       field=('wysokosc','obroty','strumien',)
=======
       field='__all__'
       exclude = ()
>>>>>>> 6deb9f7... Fixing after migrations from remote repository

class UOAP0Form(forms.ModelForm):
     
     class Meta:
         model=UOAP0
<<<<<<< HEAD
=======
         exclude = ()
>>>>>>> 6deb9f7... Fixing after migrations from remote repository

class UOAP2Form(forms.ModelForm):
     
    class Meta:
<<<<<<< HEAD
        model=UOAP2         
=======
        model=UOAP2     
        exclude = ()
>>>>>>> 6deb9f7... Fixing after migrations from remote repository
