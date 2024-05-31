
from django import forms

class LoginForm(forms.Form):
    email_or_contact = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg"}))
    error = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-lg", "hidden": True}), required=False)
    
    def clean(self):
        self.cleaned_data = super(LoginForm, self).clean()    
        return self.cleaned_data 