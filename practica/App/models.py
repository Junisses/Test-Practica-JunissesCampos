from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre_empresa  = models.TextField(max_length=50)
    rut             = models.TextField(max_length=9)
    direccion       = models.TextField(max_length=100)
    telefono        = models.TextField(max_length=9)

    def __str__(self):
        return self.nombre_empresa

class Estado(models.Model):
    estado = models.TextField(max_length=8)

    def __str__(self):
        return self.estado

class Etapa(models.Model):
    etapa = models.TextField(max_length=15)

    def __str__(self):
        return self.etapa

class Prospecto(models.Model):
    nombre          = models.TextField(max_length=50)
    mail            = models.TextField(max_length=100)
    telefono        = models.TextField(max_length=9)
    fecha_ingreso   = models.DateTimeField(auto_now_add=True)
    sexo            = models.TextField(max_length=12)
    cliente_id      = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.CASCADE)
    estado_id       = models.ForeignKey(Estado, blank=True, null=True, on_delete=models.CASCADE)
    etapa_id        = models.ForeignKey(Etapa, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    username        = models.TextField(max_length=15)
    password        = models.TextField(max_length=100)
    cliente     = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

