from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from core.views import CustomLoginView  
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tecnologias', views.TecnologiaViewSet)
router.register(r'programadores', views.ProgramadorViewSet)
router.register(r'projetos', views.ProjetoViewSet)
router.register(r'alocacoes', views.AlocacaoViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="API de Alocação de Desenvolvedores",
        default_version='v1',
        description="Documentação da API para gerenciar a alocação de desenvolvedores em projetos",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("api/custom-login/", CustomLoginView.as_view(), name="custom_login"),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', views.home, name='home'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('api/token/', obtain_auth_token, name='token_obtain_pair'),
]
