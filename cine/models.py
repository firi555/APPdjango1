from django.db import models

class Genero(models.Model):
    name = models.CharField(max_length=64,help_text='descripcion de la pelicula')

    def __str__(self):
        return self.name
class Director(models.Model):
    primer_nombre=models.CharField(max_length=100,help_text='nombre del director',default='pedro')
    segundo_nombre=models.CharField(max_length=100,help_text='apellido del director',default='perez')
    titulo=models.CharField(max_length=100,help_text='nombre de la pelicula',default='titulo')
    descripcion=models.CharField(max_length=100,help_text='describa de que trata la pelicula',default='pelicula')

    def __str__(self):
        imprime =self.primer_nombre+" "+self.segundo_nombre+"  "+"TITULO : "+self.titulo+"  "+"DESCRIPCION : "+ self.descripcion
        return imprime