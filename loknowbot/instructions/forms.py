from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import InstructionSet


class InstructionForm(forms.ModelForm):
    up = forms.IntegerField(min_value=0,
                            widget=forms.NumberInput(attrs={"class": "form-control"}),
                            help_text='Enter an integer for going UP')
    down = forms.IntegerField(min_value=0,
                              widget=forms.NumberInput(attrs={"class": "form-control"}),
                              help_text='Enter an integer for going DOWN')
    left = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={"class": "form-control"}),
                              help_text='Enter an integer for going LEFT')
    right = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={"class": "form-control"}),
                               help_text='Enter an integer for going RIGHT')


    class Meta:
        model = InstructionSet
        fields = ('up', 'down', 'left', 'right')

