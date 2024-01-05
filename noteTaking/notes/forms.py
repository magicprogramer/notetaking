from .models import *
from django import forms
from django_quill.forms import QuillFormField
class VaultForm(forms.ModelForm):
    class Meta:
        model = Vault
        fields = ['name']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", "-")
        super(VaultForm,self).__init__(*args, **kwargs)
        self.user = user

    def save(self, commit = False, *args, **kwargs):
        instance = super(VaultForm, self).save(commit, *args, **kwargs)
        instance.user= self.user
        instance.save()

class NoteForm(forms.ModelForm):
    class Meta:
        model  = Note
        fields = ["title"]
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", "-")
        vault = kwargs.pop("vault", "-")
        super(NoteForm,self).__init__(*args, **kwargs)
        self.user = user
        self.vault = vault
       # self.fields['vault'].initial = vault
    def save(self, comit = False, *args, **kwargs):
        instance = super(NoteForm, self).save(commit=False, *args, **kwargs)
        #print(self.vault)
        print(self.user)
        instance.user = self.user
        instance.vault = self.vault
        instance.save()
class ParagraphForm(forms.ModelForm):
    content = QuillFormField()
    class Meta:
        model = Pragraph
        fields = ["content"]  
    