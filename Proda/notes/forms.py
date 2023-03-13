from django import forms
from .models import *

class EditNoteForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, widget=forms.Textarea())
    content = forms.CharField(label='Content', widget=forms.Textarea())

    def clean_content(self):
        title = self.cleaned_data['content']
        if len(title) >= 0:
            title += '\n'
            return title
        
class AddDirectoryForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50)