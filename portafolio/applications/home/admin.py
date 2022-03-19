from django.contrib import admin
from .models import SobreMi, Skill, Project, Contact

# Register your models here.
admin.site.register(SobreMi)
admin.site.register(Skill)
admin.site.register(Contact)

class ProjectAdmin(admin.ModelAdmin):
    #
    filter_horizontal = ('skills',)

admin.site.register(Project, ProjectAdmin)
