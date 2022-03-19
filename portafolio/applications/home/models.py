from django.db import models
#app terceros
from model_utils.models import TimeStampedModel
# Create your models here.
class SobreMi(models.Model):
    name  = models.CharField('Nombre', max_length=50)
    description = models.TextField('Descripcion', blank=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.name


class Skill(models.Model):
    name  = models.CharField('Nombre', max_length=50)
    image = models.ImageField(upload_to='habilidades', blank=True, null=True)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
    
    def __str__(self):
     return str(self.id) + ' - ' + self.name



class Project(models.Model):
    name  = models.CharField('Nombre', max_length=50)
    description = models.TextField('Descripcion', blank=True)
    image = models.ImageField('imagen', upload_to='proyectos', blank=True, null=True)
    skills = models.ManyToManyField(Skill, verbose_name="Habilidades", blank=True)
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
        
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
     return str(self.id) + ' - ' + self.name


class Contact(TimeStampedModel):
    """ Formulario de Contacto """
    full_name = models.CharField('Nombres', max_length=60)
    email = models.EmailField()
    messagge = models.TextField()


    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'
    
    def __str__(self):
        return self.full_name