from django.urls import path, include
from .views import *

urlpatterns = [
    path('', get_notes, name='note_home'),
    path('<int:note_id>', NotesView.as_view(), name='notes'),
    path('dir/<int:dir_id>', NoteDirectoriesView.as_view(), name='notes_dir'),
    path('dir/<int:dir_id>/<int:note_id>', NoteDirectoriesView.as_view(), name='notes_dir_w_note'),
    path('add/<int:dir_id>', add_note, name='note_add'),
    path('delete/<int:dir_id>/<int:note_id>/', delete_note, name='note_delete'),
    path('edit/<int:dir_id>/<int:note_id>/', UpdateNote.as_view(), name='note_edit'),
    path('add_dir/', add_dirrectory, name='add_directory'),
]
