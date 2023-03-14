from django.shortcuts import reverse, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, FormView

from .models import *
from notes.models import *
from .utils import DataMixin
from .forms import *


def get_notes(request):
    first_note = Note.objects.filter(owner=request.user.pk).first().pk
    return HttpResponseRedirect(reverse('notes', args=[first_note]))
    

def delete_note(request, note_id):
    Note.objects.get(pk=note_id).delete()
    return HttpResponseRedirect(reverse('note_home'))


def add_note(request):
    note = Note.objects.create(title='', content='', owner=request.user)
    return HttpResponseRedirect(reverse('notes', args=[note.pk]))

def add_dirrectory(request):
    if request.method == "POST":
        form = AddDirectoryForm(request.POST)
        if form.is_valid():
            dir_title = form.cleaned_data['title']
            dir = NoteDirectory.objects.create(title=dir_title, owner=request.user)
            note = Note.objects.create(title='', owner=request.user, directory=dir)

    return HttpResponseRedirect(reverse('notes_dir', args=[dir.pk]))


class NoteDirectoriesView(DataMixin, ListView):
    model = NoteDirectory
    context_object_name = 'dirs'
    template_name = 'notes/notes.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(dir_id=self.kwargs['dir_id'])
        
        return dict(list(context.items())+list(c_def.items()))

class NotesView(DataMixin, ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        first_note = Note.objects.filter(owner=self.request.user.pk).first().pk
        try:
            self.kwargs['note_id']
        except KeyError:
            context['note_id'] = first_note
            redirect(f'notes/{first_note}/')

        context['dir_selected'] = NoteDirectory.objects.filter(owner=self.request.user.pk).first().pk
        if 'note_id' in self.kwargs:
            c_def = self.get_user_context(note_id=self.kwargs['note_id'])
        else:
            c_def = self.get_user_context(note_id=first_note)
            
        return dict(list(context.items())+list(c_def.items()))
    
class UpdateNote(DataMixin, FormView):
    form_class = EditNoteForm
    template_name = 'notes/notes.html'
    form = EditNoteForm
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(note_id=self.kwargs['note_id'])

        return dict(list(context.items())+list(c_def.items()))
    
    def form_valid(self, form):
        context = self.get_context_data()
        note_id = context['note_selected'].pk
        note = Note.objects.get(pk=note_id)
        note.title = form.cleaned_data['title']
        note.content = form.cleaned_data['content']
        note.save()
        return redirect('notes_dir_w_note', dir_id=context['dir_selected'], note_id=context['note_id'])
    
# class AddDirectory(DataMixin, FormView):
#     form_class = AddDirectoryForm
#     template_name = 'notes/notes.html'
#     form = AddDirectoryForm
    
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context()
#         return dict(list(context.items())+list(c_def.items()))
    
#     def form_valid(self, form):
#         context = self.get_context_data()
#         dir_title = form.cleaned_data['title']
#         dir_owner = self.request.user.pk
#         new_directory = NoteDirectory.objects.create()
#         return redirect('note_home')