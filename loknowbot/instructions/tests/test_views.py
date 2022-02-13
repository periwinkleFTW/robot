from django.test import TestCase
from django.urls import reverse

from ..models import InstructionSet


class InstructionListViewTest(TestCase):
    def setUp(self):
        number_of_instruction_sets = 10
        for inst_set in range(number_of_instruction_sets):
            InstructionSet.objects.create(up=1+inst_set,
                                          down=3*inst_set,
                                          left=5+inst_set,
                                          right=7-inst_set)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/instructions/list/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('instructions:instruction-set-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('instructions:instruction-set-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'instruction_set_list.html')

    def test_lists_all_authors(self):
        response = self.client.get(reverse('instructions:instruction-set-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['instruction_sets']), 10)


class TestInstructionDetailView(TestCase):
    def setUp(self):
        InstructionSet.objects.create(up=111, down=333, left=555, right=777)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/instructions/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('instructions:instruction-set-detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('instructions:instruction-set-detail', args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'instruction_set_detail.html')

    def test_view_contains_correct_data(self):
        response = self.client.get(reverse('instructions:instruction-set-detail', args='1'))
        self.assertContains(response, 'Steps in UP direction 111')
        self.assertContains(response, 'Steps in DOWN direction 333')
        self.assertContains(response, 'Steps in LEFT direction 555')
        self.assertContains(response, 'Steps in RIGHT direction 777')


class TestInstructionCreateView(TestCase):
    pass


class TestInstructionUpdateView(TestCase):
    pass