from django.shortcuts import reverse, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from .models import *
from notes.models import *
from .utils import DataMixin


def get_notes(request):
    first_note = Note.objects.filter(owner=request.user.pk).first().pk
    return HttpResponseRedirect(reverse('notes', args=[first_note]))
    

def delete_note(request, note_id):
    Note.objects.filter(pk=note_id).delete()
    first_note = Note.objects.filter(owner=request.user.pk).first().pk
    return HttpResponseRedirect(reverse('notes', args=[first_note]))

def add_note(request):
    note = Note.objects.create(title='.', content='', owner=request.user)
    return HttpResponseRedirect(reverse('notes', args=[note.pk]))


class NotesView(DataMixin, ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        first_note = Note.objects.filter(owner=self.request.user.pk).first().pk
        try:
            self.kwargs['note_id']
        except KeyError:
            redirect(f'notes/{first_note}/')

        context = super().get_context_data(**kwargs)
        
        c_def = self.get_user_context()
        redirect(f'notes/{first_note}')
        return dict(list(context.items())+list(c_def.items()))
    
