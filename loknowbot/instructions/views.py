from django.views import View
from django.views.generic import DetailView, ListView

from .models import InstructionSet
from .forms import InstructionForm


class InstructionDetailView(DetailView):
    template_name = 'instruction_set_detail.html'
    model = InstructionSet
    context_object_name = 'instruction_set'
    slug_field = 'id'

class InstructionListView(ListView):
    template_name = 'instruction_set_list.html'
    context_object_name = 'instruction_sets'
    model = InstructionSet


class InstructionCreateView(View):
    template_name = 'instruction_set_create.html'
    model = InstructionSet
    form_class = InstructionForm

