from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    def save(self, commit = True, *args, **kwargs):
        instance = super(RegisterForm, self).save(False, *args, **kwargs)
        instance.email = self.cleaned_data['email']
        instance.save()