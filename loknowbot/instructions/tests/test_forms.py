from django.test import TestCase
from django.core.exceptions import ValidationError

from ..forms import InstructionForm
from ..models import InstructionSet


class InstructionFormTest(TestCase):

    def test_field_labels(self):
        form = InstructionForm()
        # Need to check for None due to how Django renders labels
        self.assertTrue(form.fields['up'].label == 'Up' or form.fields['up'].label is None)
        self.assertTrue(form.fields['down'].label == 'Down' or form.fields['down'].label is None)
        self.assertTrue(form.fields['left'].label == 'Left' or form.fields['left'].label is None)
        self.assertTrue(form.fields['right'].label == 'Right' or form.fields['right'].label is None)

    def test_field_help_text(self):
        form = InstructionForm()
        self.assertEqual(form.fields['up'].help_text, 'Enter an integer for going UP')
        self.assertEqual(form.fields['down'].help_text, 'Enter an integer for going DOWN')
        self.assertEqual(form.fields['left'].help_text, 'Enter an integer for going LEFT')
        self.assertEqual(form.fields['right'].help_text, 'Enter an integer for going RIGHT')



