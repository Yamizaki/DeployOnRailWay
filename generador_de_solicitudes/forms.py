from django import forms

class ContactForm(forms.Form):
    asunto= forms.CharField(label='ASUNTO', max_length=100, widget=forms.TextInput(attrs={'class':"cajita"}))
    ref= forms.CharField(label='REFERENCIA', max_length=100, widget=forms.TextInput(attrs={'class':"cajita"}))

    solicitado= forms.CharField(label='SOLICITADO', max_length=100, widget=forms.TextInput(attrs={'class':"cajita"}))
    cargo_solicitado= forms.CharField(label='CARGO DEL SOLICITADO', max_length=100, widget=forms.TextInput(attrs={'class':"cajita"}))

    atencion= forms.CharField(label='ATENCION', max_length=100, widget=forms.TextInput(attrs={'class':"cajita"}))

    solicitante= forms.CharField(label='NOMBRE SOLICITANTE', max_length=100, widget=forms.TextInput(attrs={'class':"cajita"}))
    cargo_solicitante= forms.CharField(label='CARGO DEL SOLICITANTE', max_length=100, widget=forms.TextInput(attrs={'class':"cajita"}))
    dni= forms.CharField(label='DNI SOLICITANTE', max_length=100, widget=forms.TextInput(attrs={'class':"cajita"}))
    celular= forms.CharField(label='CELULAR', max_length=100, widget=forms.TextInput(attrs={'class':"cajita"}))
    direccion= forms.CharField(label='DIRECCION', max_length=100, widget=forms.TextInput(attrs={'class':"cajita"}))
    distrito= forms.CharField(label='DISTRITO', max_length=100, widget=forms.TextInput(attrs={'class':"cajita"}))
    provincia= forms.CharField(label='PROVINCIA', max_length=100, widget=forms.TextInput(attrs={'class':"cajita"}))
    departamento= forms.CharField(label='DEPARTAMENTO', max_length=100, widget=forms.TextInput(attrs={'class':"cajita"}))
    fecha= forms.CharField(label="FECHA DE SOLICITUD", max_length=100, widget=forms.TextInput(attrs={'class':"cajita"}))
    cabeza_solicitud= forms.CharField(label='ENCABEZADO DE SOLICITUD', max_length=100, widget=forms.TextInput(attrs={'class':"cajita"}))
    cuerpo_solicitud= forms.CharField(label='CUERPO DE SOLICITUD', widget=forms.Textarea(attrs={'class':'cajita2'}))
    
    