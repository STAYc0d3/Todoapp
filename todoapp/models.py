from django.db import models
from django.conf import settings

class Task(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'todo_sasks'
    )
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    objects = models.Manager()
    
    class Meta:
        ordering = ['deadline']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self) -> str:
        return self.title