from django.views import View
from django.views.generic import DetailView, ListView

from .models import InstructionSet


class InstructionSetDetailView(DetailView):
    template_name = 'instruction_set_detail.html'
    model = InstructionSet
    context_object_name = 'instruction_set'
    slug_field = 'id'

class InstructionSetListView(ListView):
    template_name = 'instruction_set_list.html'
    context_object_name = 'instruction_sets'
    model = InstructionSet


class InstructionCreateView(View):
    model = InstructionSet

