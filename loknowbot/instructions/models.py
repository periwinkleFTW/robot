from django.db import models
from django.utils.translation import gettext as _

class InstructionSet(models.Model):
    up = models.IntegerField(_('Number of steps in the UP direction'), default=0)
    down = models.IntegerField(_('Number of steps in the DOWN direction'), default=0)
    left = models.IntegerField(_('Number of steps in the LEFT direction'), default=0)
    right = models.IntegerField(_('Number of steps in the RIGHT direction'), default=0)

    class Meta:
        verbose_name = _('Instruction Set')
        verbose_name_plural = _('Instruction Sets')

    def __str__(self):
        return f'Instruction Set #{self.id}'

    def get_euclidean_dist(self):
        pass

    def get_num_of_instructions(self):
        pass
