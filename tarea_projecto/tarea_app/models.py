from django.db import models

class Tarea(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre
    
class Mimodelo(models.Model):
    campo1 = models.CharField(max_length=50)
    campo2 = models.IntegerField()
    
    

