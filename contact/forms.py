from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label="Nombre",required=True,
                         widget=forms.TextInput(attrs={'placeholder':'Ingresa tu nombre',
                                                       'class':'form-control'}))
    email=forms.EmailField(label="Email",required=True,
                           widget=forms.TextInput(attrs={'placeholder':"Ingresa tu correo",
                                                         'class':'form-control'}))
    content=forms.CharField(label="Contenido",required=True,
                        widget=forms.Textarea(attrs={'placeholder':'Ingresa tu mensaje',
                                                     'rows':3,'class':'for'}))