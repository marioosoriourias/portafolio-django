# python

# django
from django.db import models


class SkillsManager(models.Manager):
    """ procedimiento para modelo venta """
    
    def lista_habilidades(self):
        # creamos rango de fecha
        return self.filter(
            close=False,
            anulate=False
        )
    