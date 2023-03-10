from django.urls import path, include
from .views import *

urlpatterns = [
    path('', get_notes, name='note_home'),
    path('<int:note_id>', NotesView.as_view(), name='notes'),
    path('add/', add_note, name='note_add'),
    path('delete/<int:note_id>/', delete_note, name='note_delete'),
]
