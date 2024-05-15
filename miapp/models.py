from django.contrib.auth.models import User
from django.db import models


class Preferencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_plato_preferido = models.CharField(max_length=255, null=True)
    motivo_preferencia = models.TextField(null=True)
    preferido = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre_plato_preferido} - {self.usuario.username}'
