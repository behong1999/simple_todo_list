from django import forms
from django.forms.widgets import CheckboxInput, TextInput

class CreateNewList(forms.Form):
    name = forms.CharField(max_length=200 ,widget=TextInput(attrs={'class':'m-2'}))
    check = forms.BooleanField(widget=CheckboxInput(attrs={'class':'m-2'}),required=False)