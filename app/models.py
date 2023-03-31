from django.db import models


class Tutor(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    area = models.CharField(max_length=50)

    def _str_(self):
        return self.nombre

class Mensaje(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    mensaje = models.TextField(max_length=500)

    def _str_(self):
        return self.nombre
