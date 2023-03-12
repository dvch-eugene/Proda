from django.shortcuts import reverse, redirect, render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, UpdateView, FormView

from .models import *
from notes.models import *
from .utils import DataMixin
from .forms import *


def get_notes(request):
    first_note = Note.objects.filter(owner=request.user.pk).first().pk
    return HttpResponseRedirect(reverse('notes', args=[first_note]))
    

def delete_note(request, note_id):
    Note.objects.filter(pk=note_id).delete()
    first_note = Note.objects.filter(owner=request.user.pk).first().pk
    return HttpResponseRedirect(reverse('notes', args=[first_note]))


def add_note(request):
    note = Note.objects.create(title='', content='', owner=request.user)
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
    
class UpdateNote(DataMixin, FormView):
    form_class = EditNoteForm
    template_name = 'notes/notes.html'
    form = EditNoteForm
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items())+list(c_def.items()))
    
    def form_valid(self, form):
        context = self.get_context_data()
        note_id = context['note_selected'].pk
        note = Note.objects.get(pk=note_id)
        note.title = form.cleaned_data['title']
        note.content = form.cleaned_data['content']
        note.save()
        return redirect('note_home')