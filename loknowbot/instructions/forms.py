from django import forms

from .models import InstructionSet


class InstructionForm(forms.ModelForm):

    class Meta:
        model = InstructionSet

        fields = ('up', 'down', 'left', 'right')
        widgets = {
            'up': forms.NumberInput(attrs={"class": "form-control"}),
            'down': forms.TextInput(attrs={"class": "form-control"}),
            'left': forms.TextInput(attrs={"class": "form-control"}),
            'right': forms.TextInput(attrs={"class": "form-control"}),
        }