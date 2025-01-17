from django.shortcuts import render
from rest_framework import viewsets
from .models import Tecnologia, Programador, Projeto, Alocacao
from .serializers import TecnologiaSerializer, ProgramadorSerializer, ProjetoSerializer, AlocacaoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

def home(request):
    return render(request, 'home.html')

class TecnologiaViewSet(viewsets.ModelViewSet):
    queryset = Tecnologia.objects.all()
    serializer_class = TecnologiaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ProgramadorViewSet(viewsets.ModelViewSet):
    queryset = Programador.objects.all()
    serializer_class = ProgramadorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class AlocacaoViewSet(viewsets.ModelViewSet):
    queryset = Alocacao.objects.all()
    serializer_class = AlocacaoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

