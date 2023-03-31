# import form class from django
from django import forms
from .models import Mensaje
  
# create a ModelForm
class MensajeForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Mensaje
        fields = "__all__"
