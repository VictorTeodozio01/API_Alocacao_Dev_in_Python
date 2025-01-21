from django.shortcuts import render
from rest_framework import viewsets
from .models import Tecnologia, Programador, Projeto, Alocacao
from .serializers import TecnologiaSerializer, ProgramadorSerializer, ProjetoSerializer, AlocacaoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

class CustomLoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({"token": user.fixed_token}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

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

