from django.db import models
from django.conf import settings


class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Контент")
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} : {self.owner.username}"
    
    class Meta():
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['title']


class NoteDirectory(models.Model):
    #TODO:Сделать предупреждение о том, что папка не пуста, если это так и потребовать подтверждение удаления.
    title = models.CharField(max_length=255, verbose_name="Название")
    notes = models.ForeignKey('Note', on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} : {self.owner.username}"
    
    class Meta():
        verbose_name = 'Директория заметок'
        verbose_name_plural = 'Директории заметок'
        ordering = ['title']
