from django import forms
from backoffice_engine.models import *

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name","mobile_number","email","password"]
        
class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name","mobile_number","email"]   

#class Feedback(forms.ModelForm):
    #class Meta:
        #models = User
        #fields = ["user","comment"]
        