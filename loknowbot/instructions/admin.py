from django.contrib import admin

from .models import InstructionSet


class InstructionSetAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_distance', 'get_num_instr', 'up', 'down', 'left', 'right']

    class Meta:
        model = InstructionSet

    def get_distance(self, obj):
        return obj.get_euclidean_dist()
    get_distance.short_description = 'Distance travelled'

    def get_num_instr(self, obj):
        return obj.get_num_of_instructions()
    get_num_instr.short_description = '# of instructions'


admin.site.register(InstructionSet, InstructionSetAdmin)
