from django.views import View
from django.views.generic import DetailView

from .models import InstructionSet


class InstructionSetDetailView(DetailView):
    template_name = 'instruction_set_detail.html'
    model = InstructionSet
    slug_field = 'id'


class InstructionCreateView(View):
    model = InstructionSet

