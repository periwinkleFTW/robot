from django.contrib import admin

from .models import InstructionSet


class InstructionSetAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_distance','up', 'down', 'left', 'right']
    class Meta:
        model = InstructionSet

    def get_distance(self, obj):
        return obj.get_euclidean_dist()
    get_distance.short_description = 'Distance traveled'



admin.site.register(InstructionSet, InstructionSetAdmin)
