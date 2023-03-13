from .models import *

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['service_title'] = 'Заметки'
        if 'dir_id' in self.kwargs :
            note_dir = NoteDirectory.objects.get(pk=self.kwargs['dir_id'])
            context['notes'] = Note.objects.filter(directory=note_dir).filter(owner=self.request.user.pk)
            if 'note_id' in self.kwargs:
                context['note_selected'] = Note.objects.get(pk=self.kwargs['note_id'])
                context['dir_selected'] = self.kwargs['dir_id']
            else:
                context['note_selected'] = Note.objects.filter(directory=note_dir).first()
                context['note_id'] = context['note_selected']
        else:
            context['note_selected'] = Note.objects.get(pk=context['note_id'])
            context['notes'] = Note.objects.filter(owner=self.request.user.pk)
            context['note_id'] = context['note_selected']
            if 'dir_selected' in self.kwargs:
                context['dir_id'] = context['dir_selected']
            else:
                context['dir_id'] = NoteDirectory.objects.filter(owner=self.request.user.pk).first().pk

        if NoteDirectory.objects.filter(title='All notes'):
            context['directories'] = NoteDirectory.objects.filter(owner=self.request.user.pk)
        else:
            NoteDirectory.objects.create(title='All notes', notes=None, owner=self.request.user)

        # context['note_selected'] = Note.objects.get(pk=self.kwargs['note_id'])
            
            
        return context