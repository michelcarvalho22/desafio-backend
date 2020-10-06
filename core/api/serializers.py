from rest_framework.serializers import ModelSerializer
from core.models import Viagens,TipoViagem



class SerializerViagens(ModelSerializer):

    class Meta:
        model = Viagens
        fields = ('id','dt_inicio','dt_fim','tp_viagem','nota')


class SerializerTipoViagens(ModelSerializer):

    class Meta:
        model = TipoViagem
        fields = ['id','tpviagem']
