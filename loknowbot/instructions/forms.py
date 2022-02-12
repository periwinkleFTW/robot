from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import InstructionSet


class InstructionForm(forms.ModelForm):
    up = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={"class": "form-control"}))
    down = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={"class": "form-control"}))
    left = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={"class": "form-control"}))
    right = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={"class": "form-control"}))

    def clean_up(self):
        data = self.cleaned_data['up']
        if data['up'] is not int:
            raise ValidationError(_('Invalid "UP" input - steps must be whole numbers'))
        return data

    def clean_down(self):
        data = self.cleaned_data['down']
        if data['down'] is not int:
            raise ValidationError(_('Invalid "DOWN" input - steps must be whole numbers'))
        return data

    def clean_left(self):
        data = self.cleaned_data['left']
        if data['left'] is not int:
            raise ValidationError(_('Invalid "LEFT" input - steps must be whole numbers'))
        return data

    def clean_right(self):
        data = self.cleaned_data['right']
        if data['right'] is not int:
            raise ValidationError(_('Invalid "RIGHT" input - steps must be whole numbers'))
        return data


    class Meta:
        model = InstructionSet
        fields = ('up', 'down', 'left', 'right')

