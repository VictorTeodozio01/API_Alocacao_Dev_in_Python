from rest_framework import serializers
from .models import Tecnologia, Programador, Projeto, Alocacao

class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = '__all__'

class ProgramadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programador
        fields = '__all__'

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'

class AlocacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alocacao
        fields = '__all__'

    def validate(self, data):
        projeto = data['projeto']
        desenvolvedor = data['desenvolvedor']
        horas_alocadas = Alocacao.objects.filter(projeto=projeto).aggregate(total_horas=models.Sum('horas'))['total_horas'] or 0
        horas_disponiveis = projeto.horas_planejadas
        
        if horas_alocadas + data['horas'] > horas_disponiveis:
            raise ValidationError("O total de horas alocadas excede as horas planejadas para o projeto.")

        # Verificar se o desenvolvedor possui pelo menos uma das tecnologias do projeto
        tecnologias_projeto = projeto.tecnologias.all()
        tecnologias_dev = desenvolvedor.tecnologias.all()

        if not tecnologias_projeto.intersection(tecnologias_dev):
            raise ValidationError("O desenvolvedor não possui as tecnologias exigidas pelo projeto.")
        
        return data
    
    def validate_horas(self, horas):
        projeto = self.instance.projeto if self.instance else self.initial_data['projeto']
        
        if projeto.data_inicial > projeto.data_final:
            raise ValidationError("A data inicial do projeto não pode ser posterior à data final.")
        
        return horas
