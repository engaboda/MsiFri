from django import forms

class FormModel(forms.Form):
    artist = forms.CharField(max_length=300)
    title = forms.CharField(max_length=300)
    genr = forms.CharField(max_length=300)
    logo = forms.CharField(max_length=300)
