from django.contrib import admin
from myProjects.models import Project
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Project, ProjectAdmin)