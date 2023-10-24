from django.contrib import admin
from .models import Task, Project, Comment

admin.site.register(Comment)
admin.site.register(Project)
admin.site.register(Task)

