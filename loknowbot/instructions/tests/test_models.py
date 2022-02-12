from math import sqrt

from django.test import TestCase

from ..models import InstructionSet


class InstructionSetModelTest(TestCase):

    def setUp(self):
        self.test_set = InstructionSet.objects.create(up=1, down=3, left=5, right=7)

    def test_model_fields(self):
        self.assertEqual(self.test_set.up, 1)
        self.assertEqual(self.test_set.down, 3)
        self.assertEqual(self.test_set.left, 5)
        self.assertEqual(self.test_set.right, 7)

    def test_str_method(self):
        expected_object_name = f'Instruction Set #{self.test_set.id}'
        self.assertEqual(str(self.test_set), expected_object_name)

    def test_get_distance(self):
        x_dir = self.test_set.up - self.test_set.down
        y_dir = self.test_set.left - self.test_set.right
        dist = round(sqrt(x_dir**2 + y_dir**2), 1)
        self.assertEqual(self.test_set.get_euclidean_dist(), dist)

    def test_get_absolute_url(self):
        self.assertEqual(self.test_set.get_absolute_url(), '/instructions/1/')

    def test_get_num_of_instructions(self):
        self.assertEqual(self.test_set.get_num_of_instructions(), 4)


