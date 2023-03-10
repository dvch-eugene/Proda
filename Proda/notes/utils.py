from .models import *

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['service_title'] = 'Заметки'

        context['notes'] = Note.objects.filter(owner=self.request.user.pk)

        if NoteDirectory.objects.filter(title='All notes'):
            context['directories'] = NoteDirectory.objects.filter(owner=self.request.user.pk)
        else:
            NoteDirectory.objects.create(title='All notes', notes=None, owner=self.request.user)

        context['note_selected'] = Note.objects.get(pk=self.kwargs['note_id'])
            
            
        return context