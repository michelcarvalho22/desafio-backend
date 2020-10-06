from django.db import models

# Create your models here.


class TipoViagem(models.Model):
    tpviagem = models.CharField(max_length=60)

    def __str__(self):
        return self.tpviagem


class Viagens(models.Model):

    dt_inicio = models.DateTimeField()
    dt_fim = models.DateTimeField()
    tp_viagem = models.ForeignKey('core.TipoViagem',models.SET_NULL, null=True,blank=True)
    nota = models.DecimalField(max_digits=4,decimal_places=0)


    def __str__(self):
        return ('%s - %s' % self.tp_viagem,str(self.nota))

