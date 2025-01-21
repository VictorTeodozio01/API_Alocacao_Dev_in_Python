from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    fixed_token = models.CharField(max_length=512, blank=True, null=True, unique=True)

    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    def save(self, *args, **kwargs):
        if not self.fixed_token:  # Se ainda não tem um token fixo
            refresh = RefreshToken.for_user(self)
            self.fixed_token = str(refresh.access_token)
        super().save(*args, **kwargs)


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Programador(models.Model):
    nome = models.CharField(max_length=100)
    tecnologias = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    data_inicial = models.DateField()
    data_final = models.DateField()
    tecnologias = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.nome

class Alocacao(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    desenvolvedor = models.ForeignKey(Programador, on_delete=models.CASCADE)
    horas = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.desenvolvedor} em {self.projeto}"
