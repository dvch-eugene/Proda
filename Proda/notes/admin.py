from django.contrib import admin

from .models import *

class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'owner', 'directory')

admin.site.register(Note, NoteAdmin)
admin.site.register(NoteDirectory)
