from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)

    class Meta:
        model = CustomUser
        fields = [ 'email', 'password','role']
        widgets = {
        'password': forms.PasswordInput(),
    }
        labels = { 'role': 'Choose a role' }

    def save(self, commit=True):
        instance = super().save(commit=False)
        role = self.cleaned_data.get('role')
        instance.set_password(self.cleaned_data.get('password'))
        if role == '1':
            instance.is_staff = True
            instance.is_superuser = True

        if commit:
            instance.save()
        return instance

class LoginForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'required': 'Email is required.'})
    password = forms.CharField(widget=forms.PasswordInput())
    fields=['email', 'password']