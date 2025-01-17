from django.test import TestCase
from .models import Tecnologia, Programador, Projeto, Alocacao

class AlocacaoTestCase(TestCase):

    def setUp(self):
        # Criação das tecnologias
        self.tecnologia_python = Tecnologia.objects.create(nome="Python")
        self.tecnologia_js = Tecnologia.objects.create(nome="JavaScript")

        # Criação dos programadores
        self.programador = Programador.objects.create(nome="Alice")
        self.programador.tecnologias.add(self.tecnologia_python)

        # Criação do projeto
        self.projeto = Projeto.objects.create(
            nome="Projeto X",
            data_inicial="2025-01-01",
            data_final="2025-06-01"
        )
        self.projeto.tecnologias.add(self.tecnologia_python)

    def test_alocacao_com_tecnologia_compativel(self):
        alocacao = Alocacao.objects.create(
            projeto=self.projeto,
            desenvolvedor=self.programador,
            horas=20
        )
        self.assertEqual(alocacao.horas, 20)

    def test_alocacao_sem_tecnologia_compativel(self):
        self.programador.tecnologias.clear()  # Remove todas as tecnologias do programador
        with self.assertRaises(Exception):
            Alocacao.objects.create(
                projeto=self.projeto,
                desenvolvedor=self.programador,
                horas=20
            )
