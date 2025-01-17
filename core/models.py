from django.db import models

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
