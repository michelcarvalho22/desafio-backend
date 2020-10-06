from rest_framework.viewsets import ModelViewSet
from core.models import Viagens,TipoViagem
from .serializers import SerializerViagens,SerializerTipoViagens


class ViewSetViagens(ModelViewSet):
    queryset = Viagens.objects.all()
    serializer_class = SerializerViagens


class ViewSetTipoViagens(ModelViewSet):
    queryset = TipoViagem.objects.all()
    serializer_class = SerializerTipoViagens
