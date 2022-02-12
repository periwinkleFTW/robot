from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.urls import reverse

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

class InstructionCreateView(CreateView):
    template_name = 'instruction_set_create.html'
    model = InstructionSet
    form_class = InstructionForm

    def get_success_url(self):
        return reverse('instructions:instruction-set-detail', kwargs={'pk': self.object.id})

class InstructionUpdateView(UpdateView):
    template_name = 'instruction_set_update.html'
    model = InstructionSet
    form_class = InstructionForm

    def get_success_url(self):
        return reverse('instructions:instruction-set-detail', kwargs={'pk': self.object.id})

