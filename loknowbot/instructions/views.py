from django.views import View
from django.views.generic import DetailView


class InstructionSetDetailView(DetailView):
    template_name = 'instruction_set_detail.html'
    # FIXME: Add models...
    model = None
    slug_field = 'id'


class InstructionCreateView(View):
    # TODO
    pass
