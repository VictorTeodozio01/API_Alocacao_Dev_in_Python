from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

class Command(BaseCommand):
    help = 'Gera um token JWT fixo para um usuário específico'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Nome de usuário para gerar o token')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        User = get_user_model()
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Usuário '{username}' não encontrado."))
            return

        # Gera um token fixo
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)

        self.stdout.write(self.style.SUCCESS(f"Token JWT para {username}: {token}"))
