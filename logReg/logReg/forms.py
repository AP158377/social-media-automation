from xml.dom.minidom import CharacterData
from django import forms
class login_data(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


