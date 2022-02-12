from django.contrib import admin

from .models import InstructionSet


class InstructionSetAdmin(admin.ModelAdmin):
    list_display = ['id', 'up', 'down', 'left', 'right']
    class Meta:
        model = InstructionSet


admin.site.register(InstructionSet, InstructionSetAdmin)
