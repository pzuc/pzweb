from django import forms

class Contacto (forms.Form):
    nombre = forms.CharField(label='Tu nombre', max_length=100)
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'name':'mensaje', 'rows':4, 'cols':30}))
    email = forms.EmailField(label='Email')