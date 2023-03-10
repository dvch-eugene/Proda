from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     notes = models.ForeignKey('notes.Note', on_delete=models.CASCADE, null=True, verbose_name='Заметки')
#     notes_folders = models.ForeignKey('notes.NoteDirectory', on_delete=models.CASCADE, null=True, verbose_name='Заметки')

#     def __str__(self):
#         return f'{self.pk}: {self.title}'
    
#     def get_notes(self):
#         return list(self.notes)
