from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    # name = forms.CharField(max_length=100)
    # email = forms.CharField(validators=[EmailValidator()])
    # phone = forms.CharField(max_length=15)
    # subject = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = ('name', 'email', 'phone', 'subject', 'message')

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-label'}),
        'email': forms.EmailInput(attrs={'class': 'form-label'}),
        'phone': forms.TextInput(attrs={'class': 'form-label'}),
        'subject': forms.TextInput(attrs={'class': 'form-label'}),
        'message': forms.TextInput(attrs={'class': 'form-label'})
    }